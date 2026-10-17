#!/usr/bin/env python3
"""MOS API helper. Usage: mos.py METHOD /path [json-body] [--yes]
Env: MOS_URL, MOS_API_TOKEN (from ~/.hermes/.env). Paths are relative to /api/v1.
Throttles to ~5 req/s and retries 429. Non-GET requires --yes."""
import json, os, sys, time, urllib.request, urllib.error


def load_env():
    for l in open(os.path.expanduser('~/.hermes/.env')):
        k, _, v = l.strip().partition('=')
        if k in ('MOS_URL', 'MOS_API_TOKEN') and k not in os.environ:
            os.environ[k] = v


def call(method, path, body=None):
    load_env()
    data = json.dumps(body).encode() if body is not None else None
    for _ in range(5):
        time.sleep(0.2)
        r = urllib.request.Request(
            os.environ['MOS_URL'] + '/api/v1' + path, data=data, method=method.upper(),
            headers={'Authorization': 'Bearer ' + os.environ['MOS_API_TOKEN'],
                     'Content-Type': 'application/json'})
        try:
            with urllib.request.urlopen(r, timeout=30) as x:
                return x.status, x.read().decode()
        except urllib.error.HTTPError as e:
            if e.code == 429:
                time.sleep(2)
                continue
            return e.code, e.read().decode()
    return 429, 'rate limited'


if __name__ == '__main__':
    a = [x for x in sys.argv[1:] if x != '--yes']
    yes = '--yes' in sys.argv
    m, p = a[0].upper(), a[1]
    if m != 'GET' and not yes:
        sys.exit('refusing non-GET without --yes (confirm with user first)')
    s, t = call(m, p, json.loads(a[2]) if len(a) > 2 else None)
    print(s)
    try:
        print(json.dumps(json.loads(t), indent=1)[:6000])
    except Exception:
        print(t[:2000])
