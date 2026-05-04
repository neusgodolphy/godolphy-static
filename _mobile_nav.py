#!/usr/bin/env python3
"""Add hamburger nav to all pages that don't have it, and fix mobile CSS."""
import os, re, glob

BASE = '/Users/neusfigueres/godolphy-static'

# ─── HTML snippets ─────────────────────────────────────────────────────────────

HAMBURGER_WHITE = '''\
    <!-- Hamburger (mobile only) -->
    <button id="nav-hamburger" onclick="toggleMobileNav()" aria-label="Abrir menú" style="display:none;flex-direction:column;justify-content:center;gap:5px;background:none;border:none;cursor:pointer;padding:4px;">
      <span style="display:block;width:24px;height:2px;background:#fff;border-radius:2px;"></span>
      <span style="display:block;width:24px;height:2px;background:#fff;border-radius:2px;"></span>
      <span style="display:block;width:24px;height:2px;background:#fff;border-radius:2px;"></span>
    </button>'''

HAMBURGER_DARK = '''\
    <!-- Hamburger (mobile only) -->
    <button id="nav-hamburger" onclick="toggleMobileNav()" aria-label="Abrir menú" style="display:none;flex-direction:column;justify-content:center;gap:5px;background:none;border:none;cursor:pointer;padding:4px;">
      <span style="display:block;width:24px;height:2px;background:#02021e;border-radius:2px;"></span>
      <span style="display:block;width:24px;height:2px;background:#02021e;border-radius:2px;"></span>
      <span style="display:block;width:24px;height:2px;background:#02021e;border-radius:2px;"></span>
    </button>'''

MOBILE_OVERLAY = '''\
<!-- Mobile nav overlay -->
<div id="mobile-nav" style="display:none;position:fixed;inset:0;z-index:200;background:#3a0aaa;flex-direction:column;padding:24px 24px 40px;">
  <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:48px;">
    <a href="/"><img src="/wp-images/logo.png" alt="Godolphy" style="height:36px;" /></a>
    <button onclick="toggleMobileNav()" aria-label="Cerrar menú" style="background:none;border:none;cursor:pointer;padding:4px;">
      <svg width="24" height="24" viewBox="0 0 24 24" fill="none"><path d="M18 6L6 18M6 6l12 12" stroke="#fff" stroke-width="2" stroke-linecap="round"/></svg>
    </button>
  </div>
  <nav style="display:flex;flex-direction:column;gap:0;flex:1;">
    <a href="/sectores/" style="color:#fff;font-size:22px;font-weight:600;text-decoration:none;padding:18px 0;border-bottom:1px solid rgba(255,255,255,.15);">Sectores</a>
    <a href="/funcionalidades/" style="color:#fff;font-size:22px;font-weight:600;text-decoration:none;padding:18px 0;border-bottom:1px solid rgba(255,255,255,.15);">Funcionalidades</a>
    <a href="/lista-de-espera/" style="color:#fff;font-size:22px;font-weight:600;text-decoration:none;padding:18px 0;border-bottom:1px solid rgba(255,255,255,.15);">Recursos</a>
    <a href="/precio/" style="color:#fff;font-size:22px;font-weight:600;text-decoration:none;padding:18px 0;border-bottom:1px solid rgba(255,255,255,.15);">Precio</a>
  </nav>
  <div style="display:flex;flex-direction:column;gap:12px;margin-top:32px;">
    <a href="#" style="background:#EEFE3A;color:#3a0aaa;font-size:16px;font-weight:700;padding:14px 24px;border-radius:20px;text-decoration:none;text-align:center;">Demo</a>
    <a href="/lista-de-espera/" style="border:2px solid #fff;color:#fff;font-size:16px;font-weight:700;padding:14px 24px;border-radius:20px;text-decoration:none;text-align:center;">Lista de espera</a>
  </div>
</div>'''

TOGGLE_JS = '''\
<script>
function toggleMobileNav(){
  var o=document.getElementById('mobile-nav');
  var open=o.style.display==='flex';
  o.style.display=open?'none':'flex';
  document.body.style.overflow=open?'':'hidden';
}
</script>'''

# CSS to inject (before first </style>)
NAV_MOBILE_CSS = '  #nav-hamburger{display:flex!important;}\n'

# ─── helpers ───────────────────────────────────────────────────────────────────

def read(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def write(path, content):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

def fix_css(content):
    """
    1. Fix broken :last-child selector → remove :last-child
    2. Add #nav-hamburger rule to existing or new @media block
    """
    # Fix :last-child in any @media block
    content = content.replace(
        'nav>div>div:last-child{display:none!important;}',
        'nav>div>div{display:none!important;}'
    )
    content = content.replace(
        'nav>div>div:last-child{display:none!important;}nav>div{padding:0 20px!important;}',
        'nav>div>div{display:none!important;}nav>div{padding:0 20px!important;}'
    )
    # Also spaced variant
    content = re.sub(
        r'nav>div>div:last-child\{display:none!important;\}',
        'nav>div>div{display:none!important;}',
        content
    )

    # If #nav-hamburger rule already present, nothing to add
    if '#nav-hamburger' in content:
        return content

    # Try to inject inside existing @media(max-width:768px) block that hides nav ul
    # Pattern: the closing } of the block that has nav ul/nav>div inside
    # We look for the first occurrence of @media(max-width:768px) and append before its }
    # This is tricky with nested braces; use a simple heuristic:
    # Find 'nav>div{padding:0 20px!important;}' and inject hamburger line after it

    hamburger_rule = '#nav-hamburger{display:flex!important;}'

    if 'nav>div{padding:0 20px!important;}' in content:
        content = content.replace(
            'nav>div{padding:0 20px!important;}',
            'nav>div{padding:0 20px!important;}' + hamburger_rule,
            1
        )
    elif 'nav ul{display:none!important;}' in content:
        # inject after nav ul rule on same line
        content = content.replace(
            'nav ul{display:none!important;}',
            'nav ul{display:none!important;}' + hamburger_rule,
            1
        )
    else:
        # No existing nav @media block — inject new one before first </style>
        css_block = '\n  @media(max-width:768px){nav>div>ul{display:none!important;}nav>div>div{display:none!important;}nav>div{padding:0 20px!important;}#nav-hamburger{display:flex!important;}}\n'
        content = content.replace('</style>', css_block + '</style>', 1)

    return content

def inject_hamburger_dark_singleline(content, btn_html):
    """
    Single-line dark nav: ...Lista de espera</a></div></div></nav>
    Inject hamburger BEFORE the last </div></nav>
    """
    anchor = '</div></div></nav>'
    replacement = '</div>\n' + btn_html + '\n  </div>\n</nav>'
    if anchor in content:
        # Replace only the FIRST occurrence (the nav)
        return content.replace(anchor, replacement, 1)
    return content

def inject_hamburger_dark_multiline(content, btn_html):
    """
    Multi-line dark nav ends with:
        </div>
      </div>
    </nav>
    We want to inject before   </div>\n</nav>
    """
    # Pattern: 4 spaces + </div> + newline + 2 spaces + </div> + newline + </nav>
    patterns = [
        ('    </div>\n  </div>\n</nav>', '    </div>\n' + btn_html + '\n  </div>\n</nav>'),
    ]
    for old, new in patterns:
        if old in content:
            return content.replace(old, new, 1)
    return content

def inject_hamburger_light(content, btn_html):
    """
    Light sticky nav. Pattern varies but always has a buttons div closing before
    the wrapper div and nav close. We look for the buttons div close.
    The light nav buttons are:
      <a href="#" style="border:2px solid #631cff;...">Demo</a>
      <a href="/lista-de-espera/" style="background:#631cff;...">Lista de espera</a>
    followed by </div> (buttons div), </div> (wrapper), </nav>
    """
    # The light nav always ends with </div>\n  </div>\n</nav>
    # (multi-line format in all blog/legal pages)
    old = '    </div>\n  </div>\n</nav>'
    new = '    </div>\n' + btn_html + '\n  </div>\n</nav>'
    if old in content:
        return content.replace(old, new, 1)
    # Fallback: single-line style
    old2 = '</div></div></nav>'
    new2 = '</div>\n' + btn_html + '\n  </div>\n</nav>'
    if old2 in content:
        return content.replace(old2, new2, 1)
    return content

def inject_overlay_and_js(content):
    """Add mobile overlay + JS right after </nav> (the first one, the main nav)."""
    # Find first </nav> that follows the main nav (not the mobile-nav inner nav)
    # All files have </nav> as end of their main nav
    idx = content.find('</nav>')
    if idx == -1:
        return content
    # Check that this </nav> is the main nav (not inside mobile-nav already)
    # Since we haven't added mobile-nav yet, the first </nav> IS the main nav
    insert_point = idx + len('</nav>')
    return content[:insert_point] + '\n\n' + MOBILE_OVERLAY + '\n\n' + TOGGLE_JS + '\n\n' + content[insert_point:]

# ─── Main ──────────────────────────────────────────────────────────────────────

all_pages = glob.glob(os.path.join(BASE, '**', 'index.html'), recursive=True)

ok = 0
warn = 0

for path in sorted(all_pages):
    content = read(path)

    # Skip home (already has hamburger)
    if 'toggleMobileNav' in content:
        print(f'SKIP {os.path.relpath(path, BASE)} (already has hamburger)')
        continue

    is_dark_nav = 'position:absolute;top:0;left:0;right:0;z-index:50' in content
    is_light_nav = 'background:#fff;border-bottom' in content and 'sticky' in content

    if not is_dark_nav and not is_light_nav:
        print(f'WARN {os.path.relpath(path, BASE)} — nav type undetected')
        warn += 1
        continue

    # 1. Fix and/or add nav mobile CSS
    content = fix_css(content)

    # 2. Inject hamburger button into nav
    if is_dark_nav:
        btn = HAMBURGER_WHITE
        # Try single-line first, then multi-line
        if '</div></div></nav>' in content:
            content = inject_hamburger_dark_singleline(content, btn)
        else:
            content = inject_hamburger_dark_multiline(content, btn)
    else:
        btn = HAMBURGER_DARK
        content = inject_hamburger_light(content, btn)

    # 3. Add mobile overlay + JS after </nav>
    content = inject_overlay_and_js(content)

    # Verify hamburger was injected
    if 'nav-hamburger' not in content:
        print(f'WARN {os.path.relpath(path, BASE)} — hamburger NOT injected!')
        warn += 1
    elif 'mobile-nav' not in content:
        print(f'WARN {os.path.relpath(path, BASE)} — overlay NOT injected!')
        warn += 1
    else:
        write(path, content)
        print(f'OK   {os.path.relpath(path, BASE)}')
        ok += 1

print(f'\nDone. {ok} updated, {warn} warnings.')
