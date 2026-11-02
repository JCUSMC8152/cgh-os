# CGH OS 0.5.1 RC1 — initial evaluation prerelease

CGH OS is an independent Debian 13 derivative using GNOME, with original CGH Budget, CGH Workspace and desktop integration. Debian and bundled third-party software retain their copyright, licenses and trademarks. Debian does not endorse this derivative. This release is intended for evaluation on disposable virtual storage or a spare test drive, and is not a production-readiness or broad hardware certification.

## Exact candidate
- ISO: CGH-OS-0.5.1-RC1-amd64.iso; 5,470,879,744 bytes.
- ISO SHA-256: f936cb585c9928954181118a0185dcc5c8dab594bd83db82ad5e520739d74a80.
- CGH source snapshot commit: e29f9c492d1910d47fb8e3cae346162394704c2f. The public snapshot excludes private test history and diagnostics; the public repository commit may therefore differ from the recovered internal commit identity.
- Combined corresponding upstream-source tar: 8,609,679,360 bytes; SHA-256 52a2b3e2e831ac420242eafd7fb2ee004de7e701d735b0713a1f6c816f541960. Five ordered source parts contain 6,130 source files for 1,713 source/version pairs, plus catalog/checksum/readme metadata. UPSTREAM-SOURCE-CATALOG.json provides the package mapping.

## Accepted evidence and limits
| Area | Current RC1 evidence |
| --- | --- |
| Source | 60 source tests; exact source snapshot and independent archive checks passed. |
| Installation | Disposable 64 GiB virtio disk installation; UEFI installed-disk boot, actual reboot, graphical login and core app launch accepted. |
| Persistence | Synthetic Budget and Workspace records and a document persisted across reboot; private database modes 0600. |
| Desktop | Everyday, Developer, Home Lab and Security pages visually inspected. |
| Security checkpoint | ClamAV 1.4.6, continuous signature updater active, competing one-shot jobs disabled, locked root, active firewall, clean package audit at test time. This is not penetration testing or security certification. The scanner is on demand, not real-time malware blocking. |
| Recovery | See RECOVERY-ACCEPTANCE.json for the actual tested recovery method and result. No automatic rollback or full bare-metal recovery promise. |

The accepted RC1 VM uses a PC chipset, UEFI, standard VGA, virtio disk, two CPUs, 4096 MiB RAM, HPET off, and QEMU WHPX with kernel-irqchip=off. The installed OS retains its original `ro quiet splash` kernel arguments. Earlier WHPX defaults failed; `noapic` was a diagnostic step and is not a required release kernel argument. These results do not establish hardware minimum requirements or performance on all computers.

Earlier HP Pavilion dm4 testing is historical 0.5.0 evidence with subsequent maintenance, not a fresh physical installation of this RC1 ISO. Native RC1 physical hardware compatibility remains unaccepted. Secure Boot, encrypted installation, dual boot, Bluetooth, suspend/wake, audible sound quality, external displays, printers/scanners and other hardware models are outside the accepted scope. Do not disable security protections or repartition an important machine merely to try this candidate.

## Included corrections and provenance
DNS tools use Debian's bind9-dnsutils package; tracepath is registered; antivirus updating uses one continuous updater. ClamAV 1.4.6 was selected from authenticated Debian 13 proposed-update inputs. Firefox ESR and Thunderbird use the frozen Debian 153.6.0 ESR builds; ImageMagick uses deb13u13. Proposed-update repositories are not globally enabled. PACKAGES.tsv and SBOM.json identify actual bundled versions. A version number or current signatures alone does not guarantee that a package is free of vulnerabilities. Apply available Debian security updates before continued use.

## Source, licenses and maintenance
The public CGH source snapshot, exact corresponding upstream-source parts, package inventory, SBOM and license notices accompany this candidate. CGH's MIT license applies only to CGH code covered by that license; it does not relicense Debian packages, firmware, artwork or other third-party components. Preserve individual notices when redistributing. The source archive contains Debian source-package descriptors and original/packaging archives; retain the complete catalog and all five parts.

RC1 is the sole evaluation candidate covered by this publication. No production support term, compatibility warranty, response-time commitment or fixed update cadence is promised. This evaluation release may be superseded or withdrawn if defects are found. No automatic CGH release-upgrade or rollback service is claimed.

Contact for defects, source-delivery problems and security reports: admin@crawfordgroupholdings.com. Include version, hardware, reproduction steps and impact. Omit credentials, recovery keys, personal financial records and private diagnostic bundles.

## Upstream source test-fixture notice
The unmodified Debian YARA original source contains parser-test and fuzzing fixtures that Microsoft Defender flags as Backdoor:Unix/Multiverze. These are preserved as corresponding source, not installed or executable CGH OS payload. Source archives are intended for inspection/building on an isolated Linux development system. Keep endpoint protection enabled; do not add exclusions or restore quarantined content merely to reproduce this release. The ISO and source delivery have separate identities and acceptance checks.
