#!/usr/bin/env python3
"""Fix malformed logo img tags across all HTML pages.

The width/height script broke self-closing logo tags:
  BEFORE: <img src="/wp-images/logo.png" alt="Godolphy" style="height:40px;" / width="864" height="215">
  AFTER:  <img src="/wp-images/logo.png" alt="Godolphy" style="height:40px;width:auto;" />
"""

import re
import glob
import os

HTML_DIR = "/Users/neusfigueres/godolphy-static"
files = glob.glob(f"{HTML_DIR}/**/*.html", recursive=True)

LOGO_SRCS = ["logo.png", "logo-blanco.png", "logo-violeta.png", "logo-oscuro.png", "logo-gradient.png"]

def fix_logo_tag(match):
    tag = match.group(0)

    # Only fix tags whose src contains a known logo filename
    if not any(f"/wp-images/{logo}" in tag for logo in LOGO_SRCS):
        return tag

    # Remove malformed trailing: [ / (loading="lazy" )? width="NNN" height="NNN">]
    # and replace with proper />
    # Pattern: <img ...style="...;" / (loading="lazy" )?width="NNN" height="NNN">

    # Step 1: extract loading="lazy" if present after the stray /
    has_lazy = bool(re.search(r'/\s+loading="lazy"', tag))

    # Step 2: remove everything from the stray / onwards
    # The stray / appears as: style="...;" / width= or style="...;" / loading="lazy" width=
    tag = re.sub(r'\s*/\s+(?:loading="lazy"\s+)?width="\d+"\s+height="\d+">', '/>', tag)

    # Step 3: add loading="lazy" back if it was there (before />)
    if has_lazy and 'loading="lazy"' not in tag:
        tag = tag.replace('/>', 'loading="lazy" />')

    # Step 4: ensure width:auto is in the style attribute
    def add_width_auto(m):
        style_content = m.group(1)
        if 'width:auto' not in style_content:
            # Remove trailing semicolons then add ;width:auto;
            style_content = style_content.rstrip(';') + ';width:auto;'
        return f'style="{style_content}"'

    tag = re.sub(r'style="([^"]*)"', add_width_auto, tag)

    return tag

# Regex to match any <img ...> tag (including self-closing)
IMG_RE = re.compile(r'<img\b[^>]*/>', re.DOTALL)

# But our broken tags end with "> not "/>" — match those too
IMG_BROKEN_RE = re.compile(r'<img\b[^>]*(?:width="\d+"\s+height="\d+")>', re.DOTALL)

changed = 0
for fpath in sorted(files):
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content

    # Fix broken logo tags (end with width="N" height="N">)
    content = IMG_BROKEN_RE.sub(fix_logo_tag, content)

    if content != original:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        changed += 1
        print(f"Fixed: {os.path.relpath(fpath, HTML_DIR)}")

print(f"\nTotal files fixed: {changed}")
