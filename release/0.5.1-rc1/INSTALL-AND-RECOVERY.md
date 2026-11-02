# CGH OS 0.5.1 RC1 — installation, verification and recovery

This is an evaluation prerelease based on Debian 13 and GNOME. Use disposable virtual storage or a spare test drive. The installer can erase the selected drive. Back up important files independently, test a restore, disconnect unrelated drives and review the installer's final target summary.

## Verify before using
Download SHA256SUMS, SHA256SUMS.asc and CGH-OS-Release-Key.asc with the selected release assets. Independently compare the public key's full fingerprint with the authenticated CGH repository README:

`E634 449D 990A B9B0 41DD 6646 9FD2 5766 9811 E41F`

Import into a new isolated GnuPG home; inspect its fingerprint, then verify the detached signature on SHA256SUMS. Example on Linux:

```sh
mkdir -m 700 cgh-verify-keyring
gpg --homedir ./cgh-verify-keyring --import CGH-OS-Release-Key.asc
gpg --homedir ./cgh-verify-keyring --fingerprint
gpg --homedir ./cgh-verify-keyring --verify SHA256SUMS.asc SHA256SUMS
sha256sum --ignore-missing -c SHA256SUMS
```

The last command checks present files only. Do not interpret ignored missing files as delivered. Check the signed ARTIFACTS.json for the complete distributed file list. The complete ISO and complete upstream tar are reconstructed outputs, not separately uploaded release assets. The signed checksum manifest covers both complete outputs and every distributed part. A signature authenticates bytes, not quality or compatibility.

## Reconstruct the ISO
The three ISO parts are ordered `CGH-OS-0.5.1-RC1-amd64.iso.part-000`, `...part-001`, `...part-002`. Download all three; verify each part against the signed manifest before concatenation. They are not individually bootable.

Linux:
```sh
cat CGH-OS-0.5.1-RC1-amd64.iso.part-000 CGH-OS-0.5.1-RC1-amd64.iso.part-001 CGH-OS-0.5.1-RC1-amd64.iso.part-002 > CGH-OS-0.5.1-RC1-amd64.iso
sha256sum CGH-OS-0.5.1-RC1-amd64.iso
```
Windows Command Prompt (binary copy):
```bat
copy /b CGH-OS-0.5.1-RC1-amd64.iso.part-000+CGH-OS-0.5.1-RC1-amd64.iso.part-001+CGH-OS-0.5.1-RC1-amd64.iso.part-002 CGH-OS-0.5.1-RC1-amd64.iso
certutil -hashfile CGH-OS-0.5.1-RC1-amd64.iso SHA256
```
Expected complete ISO SHA-256: `f936cb585c9928954181118a0185dcc5c8dab594bd83db82ad5e520739d74a80`; exact size 5,470,879,744 bytes. Stop if any part or complete-file checksum differs. Keep existing files safe; choose a new output directory instead of overwriting an ISO.

## Corresponding upstream source
Join the five upstream-source parts in ascending order, `CGH-OS-0.5.1-RC1-Upstream-Source.tar.part-000` through `...part-004`, into `CGH-OS-0.5.1-RC1-Upstream-Source.tar`. Use binary concatenation on Windows. Verify every part and the complete file against SHA256SUMS. Expected complete tar SHA-256: `52a2b3e2e831ac420242eafd7fb2ee004de7e701d735b0713a1f6c816f541960`; size 8,609,679,360 bytes. Use an isolated Linux development environment for source inspection. The unmodified upstream YARA source includes parser-test/fuzzing fixtures flagged by Microsoft Defender; keep protection enabled and do not restore quarantined files or add exclusions. These source fixtures are not an installed OS payload. The tar includes 6,130 source files and three metadata files. Preserve its catalog and per-file checksums. CGH custom source is supplied separately in the Public-Source.tar.xz archive.

## Try and install
Write the verified ISO to a spare USB using a trusted image writer; this destroys that USB's contents. First try the live session and check your required devices. Use the graphical installer only on the intended disposable disk. Create a unique personal account, review the final erase summary, complete installation, remove the USB, boot from disk, save a small test document and restart to confirm persistence. Review available Debian security updates.

The accepted RC1 evidence is a UEFI/virtio VM, not universal Intel/AMD compatibility. See RELEASE-NOTES.md for the exact tested QEMU configuration and hardware limitations. Secure Boot, encryption, dual boot, Bluetooth, suspend/wake, audible quality, external displays and printers are unaccepted. Do not weaken security protections or modify an important system just to try RC1.

## Manual recovery: preserve files before repair
Stop applications and cleanly shut down when possible. Start an independent trusted rescue system with ext4 and tar support. Identify the installed filesystem and a separate backup destination by their actual labels, sizes and partition layout; device names vary. Never blindly reuse a test's `/dev/vd*` names. Mount the source read-only; on ext4, `ro,noload` avoids journal replay, but an unclean or damaged filesystem may require specialist handling. If read-only mounting fails, stop rather than force a write repair.

Copy your documents and complete application data directories to separate storage. Budget normally uses `~/.local/share/cgh-os/budget/budget.sqlite3`; Workspace normally uses `~/.local/share/cgh-os/workspace/projects.sqlite3`. Custom XDG_DATA_HOME changes those paths. Preserve hidden files, ownership and permissions. With the applications stopped, include SQLite sidecars if present. Workspace's saved project paths do not embed linked documents: back up the linked folders themselves as well.

Keep the backup untouched. Extract a second restored copy into a new empty directory on separate storage. Compare document contents and application records; run SQLite integrity checks where available, retain database permissions 0600 and private directory permissions 0700, and open restored data with the matching application before relying on it. If paths change, reconnect Workspace project folders deliberately; do not assume copied metadata moved linked documents.

RECOVERY-ACCEPTANCE.json records the current test: read-only access to the installed RC1 disposable disk, backup and separate restore on another disposable disk, byte comparison, both application exports matching the saved synthetic fixture, SQLite integrity and private database modes. The rescue environment was Alpine. This is not a tested CGH live-USB recovery boot, automatic rollback, bootloader repair, damaged-filesystem reconstruction, encryption recovery, reinstall or complete bare-metal restore. A reinstall can destroy data; preserve verified backups first.

## Help and security
Contact admin@crawfordgroupholdings.com with version, hardware, reproduction steps and impact. Omit passwords, recovery keys and private records. No response-time or support-duration promise is made for RC1. Debian and other included packages retain their individual licenses; LICENSE-NOTICES.tar.gz supplies notices, PACKAGES.tsv/SBOM.json identify bundled packages, and corresponding source is distributed alongside the ISO parts.
