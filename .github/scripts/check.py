#!/usr/bin/env python3
"""Repo checks: skill frontmatter, helper script compiles, no secrets/internal IPs."""
import ast
import pathlib
import re
import subprocess
import sys

root = pathlib.Path(__file__).resolve().parents[2]
errors = []

# 1. Every skill has valid frontmatter whose name matches its folder.
for skill in sorted((root / 'skills').iterdir()):
    md = skill / 'SKILL.md'
    if not md.is_file():
        errors.append(f'{skill.name}: missing SKILL.md')
        continue
    m = re.match(r'---\n(.*?)\n---\n', md.read_text(), re.S)
    if not m:
        errors.append(f'{skill.name}: no frontmatter')
        continue
    fm = dict(line.split(':', 1) for line in m.group(1).splitlines() if ':' in line)
    if fm.get('name', '').strip() != skill.name:
        errors.append(f'{skill.name}: frontmatter name != folder')
    if not fm.get('description', '').strip():
        errors.append(f'{skill.name}: empty description')
    for py in skill.rglob('*.py'):
        try:
            ast.parse(py.read_text(), filename=str(py))
        except SyntaxError as e:
            errors.append(f'{py}: {e}')

# 2. No secrets or internal addresses in tracked files.
patterns = {
    'long hex token': re.compile(r'\b[0-9a-f]{40,}\b'),
    'bearer literal': re.compile(r'Bearer\s+[A-Za-z0-9._-]{20,}'),
    'private IP': re.compile(
        r'\b(?:10\.\d+\.\d+\.\d+|192\.168\.(?!1\.50\b)\d+\.\d+'
        r'|172\.(?:1[6-9]|2\d|3[01])\.\d+\.\d+)\b'),
    'private key': re.compile(r'-----BEGIN [A-Z ]*PRIVATE KEY-----'),
}
files = subprocess.run(['git', 'ls-files'], cwd=root, capture_output=True,
                       text=True, check=True).stdout.split()
for f in files:
    p = root / f
    if p.name == 'check.py' or not p.is_file():
        continue
    text = p.read_text(errors='ignore')
    for label, rx in patterns.items():
        for m in rx.finditer(text):
            errors.append(f'{f}: {label}: {m.group(0)[:40]}')

if errors:
    print('\n'.join(errors))
    sys.exit(1)
print('ok')
