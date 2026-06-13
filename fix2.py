import pathlib, re

c = pathlib.Path('peking-blaricum/index.html').read_text('utf-8')

# Find and print lines with imgOverlay or Bekijk
for i, line in enumerate(c.splitlines(), 1):
    if 'imgOverlay' in line or 'Bekijk' in line or 'volledig' in line:
        print(f'{i}: {repr(line.strip()[:150])}')

print('\n--- Now fixing ---')

# 1. Remove the Menu Image Overlay section
c = re.sub(r'<!-- Menu Image Overlay -->.*?</script>\s*', '', c, flags=re.DOTALL)
print('After overlay removal, imgOverlay count:', c.count('imgOverlay'))

# 2. Replace any remaining imgOverlay onclick button
old_patterns = [
    'onclick="document.getElementById(\'imgOverlay\').classList.add(\'open\');document.body.style.overflow=\'hidden\'"',
    "onclick=\"document.getElementById('imgOverlay').classList.add('open');document.body.style.overflow='hidden'\"",
    'onclick="document.getElementById(\'imgOverlay\').style.display=\'block\';document.body.style.overflow=\'hidden\'"',
]
for old in old_patterns:
    if old in c:
        print(f'Found pattern: {old[:60]}...')
        c = c.replace(old, '')

# 3. Replace the button/link - find any line with Bekijk de volledige menukaart
c = re.sub(
    r'<a[^>]*>Bekijk de volledige menukaart</a>',
    '<a href="menukaart-peking-blaricum.pdf" download class="btn btn-primary btn-lg" style="display:inline-flex;">Download volledige menukaart</a>',
    c
)

# 4. Remove menu-overlay CSS if present
c = re.sub(r'/\* Menu modal overlay \*/[^@]*?(?=@media)', '', c, flags=re.DOTALL)

pathlib.Path('peking-blaricum/index.html').write_text(c, 'utf-8')

print('\nFinal checks:')
print('imgOverlay:', c.count('imgOverlay'))
print('Download volledige:', 'Download volledige' in c)
print('download attr:', 'download' in c)