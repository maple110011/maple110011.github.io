# -*- coding: utf-8 -*-
"""站点静态校验脚本（本机无 Ruby 时的快速检查，见 docs/站点维护手册.md 第四节）

用法：python scripts/validate.py
- frontmatter lint（title/date/tags 必填于集合文件）
- 内部链接与 permalink/集合 URL 审计
- Liquid 标签配平
- SCSS 编译（本机有 npx 时）
"""
import io
import glob
import os
import re
import subprocess
import sys

fail = False
HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(HERE)

# ---------- 1) frontmatter lint ----------
print('--- 1) frontmatter lint ---')
mds = (glob.glob('_pages/*.md') + glob.glob('_notes/*.md')
       + glob.glob('_logs/*.md') + glob.glob('_translations/*.md'))
for f in sorted(mds):
    s = io.open(f, encoding='utf-8').read()
    m = re.match(r'^---\r?\n(.*?)\r?\n---\r?\n', s, re.S)
    if not m:
        print('  BAD frontmatter:', f); fail = True; continue
    fm = m.group(1)
    required = ['title']
    if f.startswith(('_notes/', '_logs/', '_translations/')):
        required += ['date', 'tags']
    missing = [k for k in required
               if not re.search(r'^' + k + r':\s*\S', fm, re.M)]
    if missing:
        print('  MISSING', missing, 'in', f); fail = True
print('  checked', len(mds), 'files')

# ---------- 2) link audit ----------
print('--- 2) internal link audit ---')
perms = set()
for f in mds:
    s = io.open(f, encoding='utf-8').read()
    fm = re.match(r'^---\r?\n(.*?)\r?\n---\r?\n', s, re.S).group(1)
    pm = re.search(r'^permalink:\s*(.+)$', fm, re.M)
    if pm:
        perms.add(pm.group(1).strip())
for sub, prefix in (('_notes', '/notes/'), ('_logs', '/blog/'),
                    ('_translations', '/translations/')):
    for f in glob.glob(sub + '/*.md'):
        perms.add(prefix + os.path.basename(f)[:-3] + '/')
hrefs = set()
patterns = (['_pages/*.md', '_notes/*.md', '_logs/*.md',
             '_translations/*.md'] +
            glob.glob('_includes/**/*.html', recursive=True) +
            glob.glob('_layouts/*.html') + glob.glob('_data/*.yml'))
for pth in patterns:
    if any(ch in pth for ch in '*?['):
        files = glob.glob(pth, recursive=True)
    else:
        files = [pth]
    for fpath in files:
        s = io.open(fpath, encoding='utf-8', errors='ignore').read()
        for h in re.findall(r'href="(/[^"#]*)"', s):
            hrefs.add(h.rstrip('/'))
miss = [h for h in sorted(hrefs)
        if h and not h.startswith(('/images', '/assets'))
        and (h + '/') not in perms and h not in perms
        and h not in ('/about.html', '/about')]
for h in miss:
    print('  DANGLING:', h); fail = True
print('  permalinks:', len(perms), '| hrefs:', len(hrefs))

# ---------- 3) liquid tag balance ----------
print('--- 3) liquid tag balance ---')
for f in ('_pages/about.md', '_pages/notes.md',
          '_pages/blog.md', '_pages/translations.md'):
    s = io.open(f, encoding='utf-8').read()
    o = len(re.findall(r'{%-?\s*(?:if|for|case)\b', s))
    c = len(re.findall(r'{%-?\s*(?:endif|endfor|endcase)\b', s))
    print(f'  {f}: {o}/{c}')
    if o != c:
        print('   UNBALANCED'); fail = True

# ---------- 4) sass compile ----------
print('--- 4) sass compile ---')
scss = io.open('assets/css/main.scss', encoding='utf-8').read()
body = scss.split('---', 2)[2] if scss.startswith('---') else scss
io.open('_tmp_main.scss', 'w', encoding='utf-8').write(body)
try:
    r = subprocess.run(['npx', '-y', 'sass', '--load-path=_sass',
                        '--load-path=.', '_tmp_main.scss', '_tmp_out.css'],
                       capture_output=True, text=True, shell=True)
except FileNotFoundError:
    print('  SKIP (npx unavailable)')
    r = None
if r is not None:
    if r.returncode != 0:
        print(r.stderr[-800:]); fail = True
    else:
        n = len(io.open('_tmp_out.css', encoding='utf-8',
                        errors='ignore').read()) // 1024
        print('  compiled OK,', n, 'KB css')

for t in ('_tmp_main.scss', '_tmp_out.css', '_tmp_out.css.map'):
    if os.path.exists(t):
        os.remove(t)

print('\nRESULT:', 'FAIL' if fail else 'ALL PASS')
sys.exit(1 if fail else 0)
