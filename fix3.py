import pathlib, re

c = pathlib.Path('peking-blaricum/index.html').read_text('utf-8')

# Remove old modal CSS blocks (menu-overlay, menu-o-*)
c = re.sub(r'\.menu-overlay\s*\{[^}]*\}', '', c)
c = re.sub(r'\.menu-overlay\.open\s*\{[^}]*\}', '', c)
c = re.sub(r'\.menu-overlay-inner\s*\{[^}]*\}', '', c)
c = re.sub(r'\.menu-overlay-close\s*\{[^}]*\}', '', c)
c = re.sub(r'\.menu-overlay-close:hover\s*\{[^}]*\}', '', c)
c = re.sub(r'\.menu-o-title\s*\{[^}]*\}', '', c)
c = re.sub(r'\.menu-o-grid\s*\{[^}]*\}', '', c)
c = re.sub(r'\.menu-o-cat\s*\{[^}]*\}', '', c)
c = re.sub(r'\.menu-o-cat-title\s*\{[^}]*\}', '', c)
c = re.sub(r'\.menu-o-cat table\s*\{[^}]*\}', '', c)
c = re.sub(r'\.menu-o-cat td\s*\{[^}]*\}', '', c)
c = re.sub(r'\.menu-o-cat td\.num\s*\{[^}]*\}', '', c)
c = re.sub(r'\.menu-o-cat td\.price\s*\{[^}]*\}', '', c)
c = re.sub(r'\.menu-o-footer\s*\{[^}]*\}', '', c)
c = re.sub(r'@media\(max-width:968px\)\{\.menu-o-grid\{column-count:4\}\}', '', c)
c = re.sub(r'@media\(max-width:640px\)\{\.menu-o-grid\{column-count:3\}\}', '', c)
c = re.sub(r'@media\(max-width:400px\)\{\.menu-o-grid\{column-count:2\}\}', '', c)

# Remove old modal HTML (the entire imgOverlay div block)
c = re.sub(r'<div class="menu-overlay"[^>]*>.*?</div>\s*</div>\s*</div>', '', c, flags=re.DOTALL)

# Remove any orphaned close button HTML
c = re.sub(r'<button class="menu-overlay-close"[^>]*>.*?</button>', '', c, flags=re.DOTALL)

pathlib.Path('peking-blaricum/index.html').write_text(c, 'utf-8')

print('imgOverlay:', c.count('imgOverlay'))
print('menu-overlay:', c.count('menu-overlay'))
print('Download volledige:', 'Download volledige' in c)