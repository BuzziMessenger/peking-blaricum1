import pathlib

c = pathlib.Path('peking-blaricum/index.html').read_text('utf-8')

# Replace the volledig.html link
old = '<a href="volledig.html" target="_blank" class="btn btn-primary btn-lg" style="display:inline-flex;">Bekijk de volledige menukaart</a>'
new = """<a onclick="document.getElementById('imgOverlay').classList.add('open');document.body.style.overflow='hidden'" class="btn btn-primary btn-lg" style="display:inline-flex;border:none;cursor:pointer;">Bekijk de volledige menukaart</a>"""
c = c.replace(old, new)

# Add the image modal
modal = """
            <!-- Image Overlay -->
            <div class="menu-overlay" id="imgOverlay" onclick="if(event.target===this){this.classList.remove('open');document.body.style.overflow=''}">
                <div class="menu-overlay-inner" style="max-width:1920px;max-height:98vh;height:98vh;padding:0;background:#fff;display:flex;flex-direction:column;align-items:center;justify-content:center;overflow:hidden;">
                    <button class="menu-overlay-close" onclick="document.getElementById('imgOverlay').classList.remove('open');document.body.style.overflow=''">&times;</button>
                    <img src="menukaart-afbeelding.png" alt="Volledige Menukaart Peking Blaricum" style="max-width:100%;max-height:100%;object-fit:contain;display:block;">
                </div>
            </div>
"""

target = '<div class="menu-allergie">Heeft u een allergie? Meld het ons!</div>'
c = c.replace(target, target + modal)

pathlib.Path('peking-blaricum/index.html').write_text(c, 'utf-8')
print('volledig:', 'volledig' in c)
print('imgOverlay:', 'imgOverlay' in c)