#!/usr/bin/env python3
"""Fix footer horizontal overflow: box-sizing + mobile padding + bottom bar stacking."""
import os, glob

BASE = '/Users/neusfigueres/godolphy-static'
GUARD = 'FOOTER OVERFLOW FIX'

# Injected before first </style>
CSS_BLOCK = """
  /* ── FOOTER OVERFLOW FIX ── */
  footer{box-sizing:border-box;width:100%;overflow-x:hidden;}
  @media(max-width:768px){
    footer{padding:48px 20px 24px!important;}
    footer > div{padding:0!important;max-width:100%!important;}
    div[style*="justify-content:space-between;align-items:center"]{flex-direction:column!important;align-items:flex-start!important;gap:16px!important;}
    footer div[style*="display:flex;gap:24px"]{flex-wrap:wrap!important;}
  }
"""

def read(p):
    with open(p, encoding='utf-8') as f: return f.read()
def write(p, c):
    with open(p, 'w', encoding='utf-8') as f: f.write(c)

pages = glob.glob(os.path.join(BASE, '**', 'index.html'), recursive=True)

ok = warn = skip = 0

for path in sorted(pages):
    c = read(path)
    rel = os.path.relpath(path, BASE)

    if GUARD in c:
        skip += 1
        continue

    if '<footer' not in c:
        skip += 1
        continue

    if '</style>' not in c:
        print(f'WARN {rel} — no </style>')
        warn += 1
        continue

    c = c.replace('</style>', CSS_BLOCK + '</style>', 1)
    write(path, c)
    print(f'OK   {rel}')
    ok += 1

print(f'\nDone. {ok} updated, {warn} warnings, {skip} skipped.')
