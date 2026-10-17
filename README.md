# mos-hermes-skills

[Hermes Agent](https://hermes-agent.nousresearch.com/docs) skills for working with [MOS NAS](https://docs.mos-official.net).

> [!IMPORTANT]
> Unofficial and unsupported by the MOS project. The skills are working notes from hands-on testing against a MOS 0.6.0-stable VM. Anything marked UNTESTED/unverified has not been run.

| Skill | Purpose |
| --- | --- |
| `skills/mos-nas-vm-setup` | Run MOS in a VM (Proxmox recipe, portable image notes, pitfalls) |
| `skills/mos-nas-api` | Drive the MOS REST API: auth, rate limit, verified read/write calls, a 426-operation endpoint index, and a small helper script |

## Install

### With the Hermes CLI (repo must be public)
Add this repo as a skill source (tap), then install:

```bash
hermes skills tap add bantznet/mos-hermes-skills
hermes skills search mos-nas
hermes skills install mos-nas-api
hermes skills install mos-nas-vm-setup
```

Or install one skill directly by identifier: `hermes skills install bantznet/mos-hermes-skills/skills/mos-nas-api`.
Installs are security-scanned; inspect first with `hermes skills inspect <identifier>`.

> Status: tap/install commands are taken from the Hermes docs and not yet run against this repo (UNTESTED).

### Manually
Copy (or symlink) a skill folder into your Hermes skills directory:

```bash
cp -r skills/mos-nas-api ~/.hermes/skills/
```

`mos-nas-api` reads `MOS_URL` (e.g. `http://192.168.1.50`) and `MOS_API_TOKEN` from `~/.hermes/.env`. Create the token in MOS (admin tokens); prefer a read-only one for real hardware. Never commit it.

## License
MIT. MOS and its components keep their own licenses.
