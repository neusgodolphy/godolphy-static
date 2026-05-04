#!/usr/bin/env python3
"""Fix remaining mobile issues on all 6 sectores pages."""
import os, glob

BASE = '/Users/neusfigueres/godolphy-static'

# Rules to inject (as a new @media block, before first </style>)
# These override or supplement existing mobile CSS.
EXTRA_CSS = """\

  /* ── SECTORES MOBILE FIXES ─────────────────────────── */
  @media(max-width:768px){
    /* Hero: H1 smaller, text left-aligned */
    h1{font-size:28px!important;line-height:1.2!important;}
    section.hero-bg{padding:100px 20px 60px!important;}
    div[style*="gap:60px"] > div{text-align:left!important;}
    div[style*="gap:60px"] > div > div[style*="display:flex;gap:14px"]{justify-content:flex-start!important;}
    /* Hero image: don't stack with overflow */
    div[style*="flex:1;display:flex;justify-content:flex-end;"]{justify-content:center!important;order:2!important;width:100%!important;}
    div[style*="flex:1;max-width:580px"]{max-width:100%!important;}
    /* Feature sections: flex-direction + image always below */
    div[style*="display:flex;align-items:center;gap:80px"]{flex-direction:column!important;gap:32px!important;}
    div[style*="display:flex;align-items:center;gap:60px"]{flex-direction:column!important;gap:32px!important;}
    div[style*="display:flex;align-items:center;gap:80px"] > div{width:100%!important;max-width:100%!important;min-width:0!important;}
    div[style*="flex:1;display:flex;align-items:center;justify-content:center;"]{order:2!important;width:100%!important;}
    /* Sections: reduce top/bottom padding too */
    section[style*="padding:100px 40px"]{padding:56px 20px!important;}
    section[style*="padding:96px 40px"]{padding:56px 20px!important;}
    section[style*="padding:80px 40px"]{padding:48px 20px!important;}
    section[style*="padding:130px 40px"]{padding:100px 20px 56px!important;}
    /* CTA inner box */
    div[style*="padding:80px 60px"]{padding:40px 24px!important;}
    div[style*="border-radius:32px"]{border-radius:20px!important;}
    h2[style*="font-size:46px"]{font-size:26px!important;line-height:1.2!important;}
    /* CTA buttons: column */
    div[style*="display:flex;gap:16px;justify-content:center;flex-wrap:wrap"]{flex-direction:column!important;align-items:stretch!important;}
    /* Hero CTA buttons */
    div[style*="display:flex;gap:14px;flex-wrap:wrap"]{flex-direction:column!important;align-items:stretch!important;}
    /* Cards grids */
    div[style*="grid-template-columns:repeat(4,1fr)"]{grid-template-columns:repeat(2,1fr)!important;}
    div[style*="grid-template-columns:repeat(3,1fr)"]{grid-template-columns:1fr!important;}
    /* 3-step domicilio grid */
    div[style*="grid-template-columns:repeat(3,1fr);gap:40px"]{grid-template-columns:1fr!important;}
    /* Testimonials */
    div[style*="grid-template-columns:repeat(3,1fr);gap:32px"]{grid-template-columns:1fr!important;}
    /* Footer: single column */
    div[style*="2fr 1fr 1fr 1fr"]{grid-template-columns:1fr!important;gap:40px!important;}
    /* Footer bottom bar: stack */
    footer > div > div[style*="justify-content:space-between"]{flex-direction:column!important;gap:16px!important;text-align:center!important;}
    footer > div > div[style*="display:flex;gap:24px"]{flex-wrap:wrap!important;justify-content:center!important;}
    /* Value prop image */
    div[style*="max-width:960px"] img{border-radius:12px!important;width:100%!important;}
    /* Typography */
    h2[style*="font-size:42px"]{font-size:24px!important;line-height:1.2!important;}
    p[style*="font-size:18px"]{font-size:16px!important;}
  }
"""

def read(p):
    with open(p, encoding='utf-8') as f: return f.read()
def write(p, c):
    with open(p, 'w', encoding='utf-8') as f: f.write(c)

pages = glob.glob(os.path.join(BASE, 'sectores/*/index.html'))
pages.append(os.path.join(BASE, 'sectores/index.html'))

for path in sorted(pages):
    c = read(path)
    rel = os.path.relpath(path, BASE)

    # Skip if already patched
    if 'SECTORES MOBILE FIXES' in c:
        print(f'SKIP {rel}')
        continue

    # Inject before first </style>
    if '</style>' in c:
        c = c.replace('</style>', EXTRA_CSS + '</style>', 1)
        write(path, c)
        print(f'OK   {rel}')
    else:
        print(f'WARN {rel} — no </style> found')
