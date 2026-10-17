#!/usr/bin/env python3
"""Generate the endpoint index markdown from a MOS OpenAPI spec.

Usage: gen-index.py spec.json > skills/mos-nas-api/references/endpoints.md
"""
import json
import sys
from collections import defaultdict

doc = json.load(open(sys.argv[1]))
groups = defaultdict(list)
for path, methods in doc['paths'].items():
    for method, op in methods.items():
        tag = (op.get('tags') or ['-'])[0]
        flag = '' if method == 'get' else ' [DEL]' if method == 'delete' else ' [mut]'
        groups[tag].append(f"{method.upper():6} {path} - {op.get('summary', '')}{flag}")

version = doc.get('info', {}).get('version', '?')
out = [f"# MOS API endpoint index (spec {version}, base /api/v1)\n",
       "GET = read. [mut] = POST/PUT/PATCH. [DEL] = DELETE.\n"]
for tag in sorted(groups):
    out.append(f"\n## {tag} ({len(groups[tag])})\n")
    out += sorted(groups[tag], key=lambda s: s.split()[1])
print('\n'.join(out))
