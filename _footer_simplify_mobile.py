#!/usr/bin/env python3
"""
Mobile footer simplification:
- Hide columns 2-4 (Industrias, Funcionalidades, Recursos) on mobile
- Inject mobile-only CTA button in standard footer first column
- Remove non-linked industry spans from home footer
"""
import os, glob, re

BASE = '/Users/neusfigueres/godolphy-static'
CSS_GUARD = 'FOOTER MOBILE SIMPLIFY'
CTA_GUARD = 'footer-mobile-cta'

CSS_BLOCK = """
  /* ── FOOTER MOBILE SIMPLIFY ── */
  @media(max-width:768px){
    /* Hide nav columns: keep only col 1 (logo + contact) */
    div[style*="grid-template-columns:2fr 1fr 1fr 1fr"] > div:nth-child(n+2),
    div[style*="grid-template-columns:1fr 1fr 1fr 1fr"] > div:nth-child(n+2){display:none!important;}
    /* Force single column */
    div[style*="grid-template-columns:2fr 1fr 1fr 1fr"],
    div[style*="grid-template-columns:1fr 1fr 1fr 1fr"]{grid-template-columns:1fr!important;gap:0!important;margin-bottom:32px!important;}
    /* Show mobile CTA */
    .footer-mobile-cta{display:inline-block!important;}
  }
"""

# Mobile CTA button — injected into standard footer first column
MOBILE_CTA = (
    '<a class="footer-mobile-cta" href="/lista-de-espera/" '
    'style="display:none;margin-top:24px;background:#EEFE3A;color:#3a0aaa;'
    'font-size:15px;font-weight:700;padding:13px 28px;border-radius:16px;'
    'text-decoration:none;text-align:center;">Empieza ahora</a>'
)

# Spans to remove from home footer (non-linked industries)
DEAD_SPANS = [
    '<span style="color:rgba(255,255,255,.7);font-size:17px;">Limpieza de oficinas</span>',
    '<span style="color:rgba(255,255,255,.7);font-size:17px;">Limpieza industrial</span>',
    '<span style="color:rgba(255,255,255,.7);font-size:17px;">Limpieza de vehículos</span>',
    '<span style="color:rgba(255,255,255,.7);font-size:17px;">Técnicos de campo</span>',
    '<span style="color:rgba(255,255,255,.7);font-size:17px;">Manitas a domicilio</span>',
    '<span style="color:rgba(255,255,255,.7);font-size:17px;">Jardineros</span>',
    '<span style="color:rgba(255,255,255,.7);font-size:17px;">Lampistas</span>',
    '<span style="color:rgba(255,255,255,.7);font-size:17px;">Fontaneros</span>',
    '<span style="color:rgba(255,255,255,.7);font-size:17px;">Mantenimiento de piscinas</span>',
    '<span style="color:rgba(255,255,255,.7);font-size:17px;">Niñeras</span>',
    '<span style="color:rgba(255,255,255,.7);font-size:17px;">Tutores a domicilio</span>',
]

def read(p):
    with open(p, encoding='utf-8') as f: return f.read()
def write(p, c):
    with open(p, 'w', encoding='utf-8') as f: f.write(c)

pages = glob.glob(os.path.join(BASE, '**', 'index.html'), recursive=True)
ok = warn = skip = 0

for path in sorted(pages):
    c = read(path)
    rel = os.path.relpath(path, BASE)
    changed = False

    # Skip if already simplified
    if CSS_GUARD in c:
        skip += 1
        continue

    has_2fr = 'grid-template-columns:2fr 1fr 1fr 1fr' in c
    has_4eq = 'grid-template-columns:1fr 1fr 1fr 1fr' in c
    is_home = (rel == 'index.html')

    if not has_2fr and not has_4eq:
        skip += 1
        continue

    # 1. Inject CSS
    if '</style>' in c:
        c = c.replace('</style>', CSS_BLOCK + '</style>', 1)
        changed = True

    # 2. Remove dead industry spans from home footer
    if is_home:
        for span in DEAD_SPANS:
            if span in c:
                c = c.replace(span, '')
        changed = True

    # 3. Inject mobile CTA into standard footer (not home — home already has CTA)
    if not is_home and CTA_GUARD not in c:
        # Standard footer: first col ends with logo+tagline </p></div>
        # before the second <div><h4 (INDUSTRIAS column)
        # Pattern: tagline paragraph closes, then first col div closes
        anchor = 'El software de reservas con IA para negocios de servicios.</p></div>'
        if anchor in c:
            c = c.replace(anchor, anchor[:-6] + MOBILE_CTA + '</div>', 1)
            changed = True
        else:
            # Fallback: try to find logo img and inject after its container div
            print(f'WARN {rel} — CTA anchor not found')
            warn += 1

    if changed:
        write(path, c)
        print(f'OK   {rel}')
        ok += 1
    else:
        print(f'skip {rel}')
        skip += 1

print(f'\nDone. {ok} updated, {warn} warnings, {skip} skipped.')
