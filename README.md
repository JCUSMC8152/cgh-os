# CGH OS

CGH OS 0.5.1 RC1 is a Debian 13 / GNOME **evaluation prerelease**.

[Download the initial evaluation release](https://github.com/JCUSMC8152/cgh-os/releases/tag/v0.5.1-rc1)

Public delivery acceptance passed on 2026-11-02T01:47:23.377746+00:00: all 25 distribution files downloaded anonymously, signed checksums and complete ISO/source hashes matched, and altered material was rejected. See [verification receipt](release/0.5.1-rc1/PUBLIC-VERIFICATION.json).

Start with [installation, reconstruction, verification and recovery instructions](release/0.5.1-rc1/INSTALL-AND-RECOVERY.md) and [release notes](release/0.5.1-rc1/RELEASE-NOTES.md). Download all three ordered ISO parts and the accompanying signed manifest from the release. Exact corresponding upstream source is supplied in five ordered parts, alongside the CGH source archive, package/SBOM inventories and license notices. GitHub's two automatic repository source archives are outside the signed 25-file distribution and do not replace the corresponding source delivery.

ISO: 5,470,879,744 bytes; SHA-256 `f936cb585c9928954181118a0185dcc5c8dab594bd83db82ad5e520739d74a80`. CGH source identity: `e29f9c492d1910d47fb8e3cae346162394704c2f`.

Release signing fingerprint: `E634 449D 990A B9B0 41DD 6646 9FD2 5766 9811 E41F`. Verify the fingerprint through a trusted channel before trusting the downloaded key.

Accepted scope includes the documented RC1 installed VM boot, actual reboot persistence, graphical authentication and application launches, 60 source tests, and manual synthetic data recovery to separate disposable storage. Recovery does not establish live-USB recovery boot, damaged filesystem repair, encryption recovery, bootloader repair or bare-metal rollback. Earlier HP hardware evidence belongs to an earlier candidate.

Secure Boot, encrypted installation, dual boot, Bluetooth without a detected controller, suspend/wake, audible quality, external displays and printers remain unaccepted. Broader hardware compatibility is not established. This is not a complete security certification.

Debian attribution and third-party license notices accompany the release. Public upstream source may contain security test fixtures; preserve them as source and do not execute them as installation steps.

Support and security contact: admin@crawfordgroupholdings.com. No response-time or support-duration promise is made.
