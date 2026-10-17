#!/usr/bin/env python3
"""MOS API helper.

Usage: mos.py --url http://<mos-ip> --token-file PATH METHOD /path [json-body] [--yes]

Paths are relative to /api/v1. Throttles to ~5 req/s and retries on 429.
Non-GET requests require --yes (confirm with the user first).
The token file holds just the bearer token (keep it chmod 600).
"""
import argparse
import json
import sys
import time
import urllib.error
import urllib.request


def call(url, token, method, path, body=None):
    data = json.dumps(body).encode() if body is not None else None
    for _ in range(5):
        time.sleep(0.2)
        req = urllib.request.Request(
            url.rstrip('/') + '/api/v1' + path, data=data, method=method.upper(),
            headers={'Authorization': 'Bearer ' + token,
                     'Content-Type': 'application/json'})
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                return resp.status, resp.read().decode()
        except urllib.error.HTTPError as e:
            if e.code == 429:
                time.sleep(2)
                continue
            return e.code, e.read().decode()
    return 429, 'rate limited'


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--url', required=True)
    ap.add_argument('--token-file', required=True)
    ap.add_argument('--yes', action='store_true')
    ap.add_argument('method')
    ap.add_argument('path')
    ap.add_argument('body', nargs='?')
    a = ap.parse_args()
    if a.method.upper() != 'GET' and not a.yes:
        sys.exit('refusing non-GET without --yes (confirm with the user first)')
    token = open(a.token_file).read().strip()
    status, text = call(a.url, token, a.method, a.path,
                        json.loads(a.body) if a.body else None)
    print(status)
    try:
        print(json.dumps(json.loads(text), indent=1)[:6000])
    except ValueError:
        print(text[:2000])


if __name__ == '__main__':
    main()
