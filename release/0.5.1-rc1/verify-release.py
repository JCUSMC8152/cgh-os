#!/usr/bin/env python3
"""Verify the complete CGH OS evaluation release; no network or writes to artifacts."""
import argparse, hashlib, json, pathlib, subprocess, tempfile, sys
FINGERPRINT = "E634449D990AB9B041DD66469FD257669811E41F"
def run(root):
    root = root.resolve()
    with tempfile.TemporaryDirectory(prefix="cgh-release-keyring-") as d:
        key = root / "CGH-OS-Release-Key.asc"
        result = subprocess.run(["gpg", "--batch", "--homedir", d, "--with-colons", "--import-options", "show-only", "--import", str(key)], capture_output=True, text=True, check=True)
        fingerprints = [line.split(":")[9] for line in result.stdout.splitlines() if line.startswith("fpr:")]
        if not fingerprints or fingerprints[0] != FINGERPRINT:
            raise ValueError("Release key fingerprint differs")
        subprocess.run(["gpg", "--batch", "--homedir", d, "--import", str(key)], capture_output=True, check=True)
        subprocess.run(["gpgv", "--keyring", str(pathlib.Path(d)/"pubring.kbx"), str(root/"SHA256SUMS.asc"), str(root/"SHA256SUMS")], capture_output=True, check=True)
    sums = {}
    for line in (root/"SHA256SUMS").read_text().splitlines():
        digest, name = line.split("  ", 1)
        if len(digest) != 64 or any(c not in "0123456789abcdef" for c in digest) or pathlib.PurePath(name).name != name or name in sums:
            raise ValueError("Invalid or duplicate checksum entry")
        sums[name] = digest
    def digest_file(name, combined=None):
        p = root/name
        if p.is_symlink() or not p.is_file(): raise ValueError("Missing regular artifact: " + name)
        h = hashlib.sha256()
        with p.open("rb") as stream:
            while data := stream.read(4*1024*1024):
                h.update(data)
                if combined is not None: combined.update(data)
        if h.hexdigest() != sums.get(name): raise ValueError("Checksum differs: " + name)
        print("PASS " + name, flush=True)
    digest_file("ARTIFACTS.json")
    inventory = json.loads((root/"ARTIFACTS.json").read_text())
    expected = inventory["distributed_files"]
    if len(expected) != len(set(expected)): raise ValueError("Duplicate distributed artifact")
    grouped = set()
    for group in inventory["assembled_files"]:
        h = hashlib.sha256()
        for name in group["parts"]:
            if name in grouped: raise ValueError("Part occurs in more than one group")
            digest_file(name, h); grouped.add(name)
        if h.hexdigest() != sums.get(group["file"]): raise ValueError("Combined checksum differs: " + group["file"])
        print("PASS reconstructed bytes " + group["file"], flush=True)
    for name in expected:
        if name not in grouped and name not in {"SHA256SUMS", "SHA256SUMS.asc", "ARTIFACTS.json"}: digest_file(name)
    if set(sums) != (set(expected)-{"SHA256SUMS", "SHA256SUMS.asc"}) | {g["file"] for g in inventory["assembled_files"]}:
        raise ValueError("Manifest and artifact inventory differ")
    print("PASS complete release: signature, all distributed bytes and both complete reconstructed checksums")
if __name__ == "__main__":
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument("directory",nargs="?",type=pathlib.Path,default=pathlib.Path("."));args=parser.parse_args()
    try: run(args.directory)
    except Exception as error:
        print("FAIL: " + str(error), file=sys.stderr);sys.exit(1)
