#!/usr/bin/env python3
"""Scan <subject>/pr-<N>/ and write a noindex catalogue at the repo root."""
from __future__ import annotations

import os
import re

ROOT = os.path.dirname(os.path.abspath(__file__))
SUBJECTS = [
    ('physics', '物理', 'https://eju.feather0.com/physics/'),
    ('chemistry', '化学', 'https://chemistry.eju.feather0.com/'),
    ('biology', '生物', 'https://biology.eju.feather0.com/'),
    ('calculus', '数学', 'https://math.eju.feather0.com/'),
]
PR_RE = re.compile(r'^pr-(\d+)$')


def find_previews():
    found = []
    for subject, label, prod in SUBJECTS:
        base = os.path.join(ROOT, subject)
        if not os.path.isdir(base):
            continue
        for name in sorted(os.listdir(base), key=lambda n: int(PR_RE.match(n).group(1)) if PR_RE.match(n) else 0):
            m = PR_RE.match(name)
            if not m or not os.path.isdir(os.path.join(base, name)):
                continue
            rel = f'{subject}/{name}/'
            links = []
            if subject == 'physics' and os.path.isdir(os.path.join(base, name, 'physics')):
                links.append(('课程首页', f'{rel}physics/'))
                links.append(('四科总入口（预览副本）', rel))
            else:
                links.append(('首页', rel))
            found.append((label, int(m.group(1)), subject, prod, links))
    return found


def render(items):
    if items:
        lis = []
        for label, num, subject, prod, links in items:
            parts = '　'.join(f'<a href="/eju-preview/{href}">{title}</a>' for title, href in links)
            lis.append(
                f'<li><span>{label}　PR #{num}</span>'
                f'<span class="links">{parts}'
                f'　<a href="{prod}">正式站</a></span></li>'
            )
        listing = '<ul class="previews">\n' + '\n'.join(lis) + '\n</ul>'
    else:
        listing = '<p class="empty">目前没有在线的预览。</p>'
    return f'''<!doctype html>
<html lang="zh-Hans">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>EJU 预览站</title>
<style>
  :root {{ --paper:#f6f4ec; --ink:#1c1a16; --ink2:#5c574e; --line:#c9c2b3; --iro:#2b4c7e; }}
  * {{ box-sizing:border-box; }}
  body {{ margin:0; background:var(--paper); color:var(--ink);
    font:16px/1.7 "Source Han Serif SC","Noto Serif SC","Songti SC",serif; }}
  .iro {{ height:3px; background:var(--iro); }}
  main {{ max-width:42rem; margin:0 auto; padding:2.2rem 1.4rem 4rem; }}
  .eyebrow {{ font-size:12px; letter-spacing:.14em; color:var(--ink2); margin:0; }}
  h1 {{ font-weight:600; font-size:1.85rem; margin:.35rem 0 .7rem; }}
  hr {{ border:0; border-top:1px solid var(--ink); margin:1.1rem 0 1.3rem; }}
  .note, .empty {{ color:var(--ink2); }}
  a {{ color:var(--iro); text-decoration-thickness:1px; text-underline-offset:.15em; }}
  ul.previews {{ list-style:none; padding:0; margin:1.2rem 0 0; }}
  ul.previews li {{ margin:0; padding:.7rem 0; border-top:1px solid var(--line); }}
  ul.previews li:last-child {{ border-bottom:1px solid var(--line); }}
  ul.previews .links {{ display:block; font-size:.95rem; }}
</style>
</head>
<body>
<div class="iro"></div>
<main>
<p class="eyebrow">EJU　PREVIEW</p>
<h1>测试预览</h1>
<hr>
<p class="note">这里是 PR 预览站，不是正式站，请不要把它当成发布地址。搜索引擎也不应收录这里的页面。正式站是 <a href="https://eju.feather0.com/">eju.feather0.com</a>。</p>
{listing}
</main>
</body>
</html>
'''


def main():
    html = render(find_previews())
    dest = os.path.join(ROOT, 'index.html')
    open(dest, 'w', encoding='utf-8').write(html)
    print(f'wrote {dest} ({len(find_previews())} previews)')


if __name__ == '__main__':
    main()
