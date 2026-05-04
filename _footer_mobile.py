#!/usr/bin/env python3
"""Add footer 4-column grid mobile fix to all pages that need it."""
import os, glob

BASE = '/Users/neusfigueres/godolphy-static'
GUARD = 'FOOTER GRID MOBILE FIX'

def read(p):
    with open(p, encoding='utf-8') as f: return f.read()
def write(p, c):
    with open(p, 'w', encoding='utf-8') as f: f.write(c)

pages = glob.glob(os.path.join(BASE, '**', 'index.html'), recursive=True)

ok = warn = skip = 0

for path in sorted(pages):
    c = read(path)
    rel = os.path.relpath(path, BASE)

    # Skip if already patched
    if GUARD in c:
        skip += 1
        continue

    has_2fr = 'grid-template-columns:2fr 1fr 1fr 1fr' in c
    has_4eq = 'grid-template-columns:1fr 1fr 1fr 1fr' in c

    if not has_2fr and not has_4eq:
        skip += 1
        continue

    rules = []
    if has_2fr:
        rules.append('div[style*="grid-template-columns:2fr 1fr 1fr 1fr"]{grid-template-columns:1fr!important;gap:32px!important;}')
    if has_4eq:
        rules.append('div[style*="grid-template-columns:1fr 1fr 1fr 1fr"]{grid-template-columns:1fr 1fr!important;gap:32px!important;}')

    block = (
        '\n  /* ── ' + GUARD + ' ── */\n'
        '  @media(max-width:768px){\n'
        + ''.join('    ' + r + '\n' for r in rules)
        + '  }\n'
    )

    if '</style>' in c:
        c = c.replace('</style>', block + '</style>', 1)
        write(path, c)
        print(f'OK   {rel}')
        ok += 1
    else:
        print(f'WARN {rel} — no </style>')
        warn += 1

print(f'\nDone. {ok} updated, {warn} warnings, {skip} skipped.')
