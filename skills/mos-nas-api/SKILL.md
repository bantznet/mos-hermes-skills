---
name: mos-nas-api
description: Use when managing an existing, running MOS NAS (pools, shares, disks, services) through its REST API.
---

# Manage a running MOS NAS via its REST API

For a MOS server that is already installed and reachable. Not an install guide. Spec: MOS API 0.1.0, 426 operations. Swagger UI at `http://<mos>/api-docs/`; the spec is embedded as JSON in `/api-docs/swagger-ui-init.js` (there is no `/openapi.json`). Endpoint index: `references/endpoints.md`.

## Access
- Base `http://<mos>/api/v1` (also port 998). Header `Authorization: Bearer <token>`.
- Tokens: `POST /auth/login` (JWT, optional MFA) or `/auth/admin-tokens` (per-token permissions; use a read-only one for monitoring). `GET /auth/admin-tokens/me` verifies it. `/users/me` and `/auth/profile` 404 for admin tokens.
- Keep the token in a file only you can read (e.g. `~/.config/mos/token`, chmod 600). Helper: `python3 <skill-dir>/scripts/mos.py --url http://<mos> --token-file ~/.config/mos/token GET /pools`. Non-GET needs `--yes`.

## Rate limit
20 requests per 1s window. A burst makes every call return 429 for up to about a minute. Pace at 5 req/s or less and retry 429 after a short sleep (the helper does). Responses carry `RateLimit-Remaining` / `RateLimit-Reset`.

## Read calls (verified 200)
`/mos/osinfo`, `/mos/services`, `/mos/settings/system`, `/system/load`, `/system/memory`, `/system/detailed`, `/disks`, `/pools`, `/pools/{id}/status`, `/shares`, `/nut/status`, `/notifications`, `/lxc/containers`, `/docker/mos/*`, `/vm/machines`, `/mos/plugins`, `/mos/zram/status`.
- Docker/LXC/VM endpoints error (500/404) until the service is enabled in MOS settings.
- `/mos/hub/*` and `/system/sensors` returned 500/400 on a VM (hub index not loaded, no hardware sensors); not checked on bare metal.
- `/mos/download`, `/mos/readfile`, `/system/logs/content` need query params; `/mos/diag` downloads a tar.gz.

## Safety
- Default to read-only. Get explicit per-action confirmation before: pool create/format/delete, disk operations, share delete, user/token delete, power/update calls under `/mos/*`, Terminal endpoints.
- Identify disks by `serial`, never by `/dev/sdX` alone: letters can reshuffle across restarts. Re-read `GET /disks` right before any pool call and confirm the target is blank.
- A pool hosting Docker/LXC/VM data can't be unmounted or deleted (400 'in use by ...'); stop the services first. `force=true` exists; don't use it without confirmation.
- WebSocket endpoints aren't usable via the helper; use the REST equivalents.

## Verified writes
- **Single pool:** `POST /pools/single` `{"name","device","filesystem":"xfs","format":true,"options":{"automount":true}}` returns 201 and mounts at `/mnt/<name>`.
- **mergerfs + SnapRAID:** `POST /pools/mergerfs` `{"name","devices":[...],"filesystem":"xfs","format":true,"options":{"automount":true,"minfreespace":"1G"}}` (default `minfreespace` is 20G; lower it on small disks). Parity is added after creation: `POST /pools/{id}/parity/add` `{"devices":["/dev/sdX"],"format":true}` (parity >= largest data disk unless `skip_size_check`; mounts at `/var/snapraid/<pool>/parity1`).
- **SnapRAID run:** `POST /pools/{id}/parity` `{"operation":"sync|check|scrub|fix|status|force_stop"}` (key is `operation`). Async, one at a time per pool (a second returns 400 'already running'). Watch `GET /pools/{id}/status` (`parity_operation`, `parity_progress`). Schedules: pool config `sync` / `check` / `scrub` (cron strings, off by default), edit via `PATCH /pools/{id}/config`.
- **SMB share:** `POST /shares/smb` `{"shareName","poolName","subPath","guest_ok":true}` returns 201 and restarts SMB. `DELETE /shares/smb/{id}` returns 200 and leaves the folder on disk. NFS follows the same pattern at `/shares/nfs`.

## Unverified
A SnapRAID sync running to completion (one sat in 'preparing' for minutes on an empty pool), pool delete, SMB client access, MFA login, token permission modes, and all other mutation bodies. Read the schema in the spec before calling any other write.

## Regenerating the index
Fetch `swagger-ui-init.js`, parse JSON after `"swaggerDoc"` with `json.JSONDecoder().raw_decode`, group `paths` by first tag.
