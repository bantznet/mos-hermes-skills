# mos-hermes-skills

[Hermes Agent](https://hermes-agent.nousresearch.com/docs) skills for working with [MOS NAS](https://docs.mos-official.net).

> [!IMPORTANT]
> Unofficial and unsupported by the MOS project. The skill is working notes from hands-on testing against a MOS 0.6.0-stable VM. Anything marked UNTESTED/unverified has not been run.

One skill, for when you **already have a running MOS server** and want your agent to manage it:

| Skill | Purpose |
| --- | --- |
| `skills/mos-nas-api` | Manage MOS through its REST API: auth, rate limit, safety rules, verified read/write calls, a 426-operation endpoint index, and a small helper script |

## Install

### With the Hermes CLI
Add this repo as a skill source (tap), then install:

```bash
hermes skills tap add bantznet/mos-hermes-skills
hermes skills search mos-nas
hermes skills install mos-nas-api
```

Or install one skill directly by identifier: `hermes skills install bantznet/mos-hermes-skills/skills/mos-nas-api`.
Installs are security-scanned; inspect first with `hermes skills inspect <identifier>`.

> Status: tested on Hermes with a clean skills directory. Both skills install with a SAFE scan verdict.

### Manually
Copy (or symlink) a skill folder into your Hermes skills directory:

```bash
cp -r skills/mos-nas-api ~/.hermes/skills/
```

`mos-nas-api` needs the MOS base URL and an admin API token. Save the token to a file only you can read (e.g. `~/.config/mos/token`, chmod 600) and pass `--url` and `--token-file` to `scripts/mos.py`. Prefer a read-only token on real hardware. Never commit it.

## License
MIT. MOS and its components keep their own licenses.
