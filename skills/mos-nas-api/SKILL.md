---
name: mos-nas-api
description: Use when querying or managing a MOS NAS over its REST API.
---

# MOS NAS REST API

Spec: 426 operations, MOS API 0.1.0. Swagger UI at `http://<mos>/api-docs/`; the spec is embedded as `swaggerDoc` JSON in `/api-docs/swagger-ui-init.js` (there is no `/openapi.json`; those URLs return the SPA HTML). Full index: `references/endpoints.md`. Install/VM setup: see `mos-nas-vm-setup`.

## Access
- Base `http://<mos>/api/v1` (also port 998). Env in `~/.hermes/.env`: `MOS_URL`, `MOS_API_TOKEN`.
- Auth: `Authorization: Bearer <token>`. Tokens come from `POST /auth/login` (JWT, optional MFA) or `/auth/admin-tokens` (per-token permission modes; create a read-only one for real hardware).
- `GET /auth/admin-tokens/me` verifies the token. `/users/me` and `/auth/profile` 404 for admin tokens (no user).
- Helper: `python3 ~/.hermes/skills/mos-nas-api/scripts/mos.py GET /pools`. Non-GET needs `--yes`.

## Rate limit (pitfall)
20 requests per 1s window (`RATE_LIMIT_MAX/WINDOW` in `/boot/config/api/env`; docs say don't change). A burst sweep makes everything return 429 for a while. Pace at <=5 req/s and retry 429 with a short sleep. Counters reset on API/server restart. Responses carry `RateLimit-Remaining` / `RateLimit-Reset` headers; the 429 clears within about a minute.

## Safe read calls (verified 200 on the test VM)
`/mos/osinfo`, `/mos/services`, `/mos/settings/system`, `/system/load`, `/system/memory`, `/system/detailed`, `/disks`, `/pools`, `/pools/availablepooltypes`, `/shares` (`{smb,nfs}`), `/nut/status`, `/notifications`, `/lxc/containers`, `/mos/plugins`, `/mos/zram/status`. 99 parameterless GETs returned 200 in total.
- 500s on a fresh install: Docker/LXC/VM endpoints return 200 once those services are enabled in MOS settings (verified: enabling them fixed `/docker/mos/*`, `/vm/machines`, `/vm/index`, `/vm/machines/usage`; `/docker/mos/containers` 404 was also the disabled state). Still 500/400 with them on: `/mos/hub/categories|types|index` (hub index likely not fetched/configured) and `/system/sensors`, `/mos/sensors/unmapped` (a VM has no hardware sensors).
- `/mos/download`, `/mos/readfile`, `/system/logs/content` need query params; `/mos/diag` downloads a tar.gz.

## Mutation rules
- Default to read-only. Pool create/format/destroy, disk ops, share delete, user/token delete, power/update endpoints under `/mos/*`, and Terminal endpoints need explicit per-action confirmation from the user, (even on a throwaway VM; this skill is meant for real hardware too).
- WebSocket groups (Disks, Docker, LXC, NUT, Pools, VM, System load, Terminal, File operations) are not usable via the helper; use REST equivalents.
- Candidate MCP promotion: a read-only subset via MetaMCP, only if reused across clients.

## Verified write: mergerfs + SnapRAID parity
`POST /pools/mergerfs` body `{"name","devices":[...],"filesystem":"xfs","format":true,"options":{"automount":true,"minfreespace":"1G"}}`: the default `minfreespace` is 20G, so set it lower on small disks. There is no parity field on create; add parity afterwards with `POST /pools/{id}/parity/add` `{"devices":["/dev/sdX"],"format":true}` (parity must be >= the largest data disk unless `skip_size_check`). Parity mounts at `/var/snapraid/<pool>/parity1`; the pool's total space counts data disks only.
SnapRAID runs on demand via `POST /pools/{id}/parity` `{"operation":"sync|check|scrub|fix|status|force_stop"}` (the field is `operation`, not `command`; a wrong key returns 400 'Operation is required'). Schedules live in the pool config under `sync`, `check` and `scrub` (cron strings, disabled by default); edit with `PATCH /pools/{id}/config`. Operations are async and one at a time per pool (a second returns 400 'already running', socket `/run/snapraid/<pool>.socket`); watch `GET /pools/{id}/status` (`parity_operation`, `parity_progress`). Unverified: a sync running to completion (a `status` run sat in 'preparing' for minutes).

## Verified write: create a single pool
Device letters (/dev/sdX) can reshuffle across reboots (the boot disk and a data disk swapped); identify disks by `serial` and re-read `GET /disks` right before any pool call. New disks only appear after a guest reboot. Enabling Docker/LXC/VM puts their data on a pool, and MOS then refuses to unmount/delete it (400 'in use by Docker...'; stop services or pass force=true).
`POST /pools/single` body `{"name":"testpool","device":"/dev/sda","filesystem":"xfs","format":true,"options":{"automount":true,"comment":"..."}}` returns 201, formats, and mounts at `/mnt/<name>` immediately (the response lists the actual partition, e.g. /dev/sda1). Check the target is blank first (`GET /disks`; the boot disk shows a partition mounted at `/boot`). Other pool types use `/pools/{multi,mergerfs,bcachefs,nonraid}`; read the schema in the spec before calling. Delete path not yet tested.

## Verified write: SMB share create/delete
`POST /shares/smb` body `{"shareName":"apitest","poolName":"testpool","subPath":"apitest","guest_ok":true}` returns 201 (path `/mnt/<pool>/<subPath>`, SMB restarted). `DELETE /shares/smb/{id}` returns 200; `directoryDeleted:false`, so the folder stays on disk. Share id comes from the create response or `GET /shares/smb`. Not verified: actual SMB client access (no smbclient on the agent VM). NFS uses the same pattern at `/shares/nfs`.

## Regenerating the index
Fetch `swagger-ui-init.js`, parse JSON after `"swaggerDoc"` with `json.JSONDecoder().raw_decode`, group `paths` by first tag.

## Unverified
Other mutation bodies, pool delete, MFA login flow, token permission modes, and WebSocket usage have not been exercised.
