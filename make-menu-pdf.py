from PIL import Image, ImageDraw, ImageFont
import os

# Create a multi-page PDF: page 1 = afhaalmenu, page 2-3 = menukaart
W, H = 2480, 3508  # A4 at 300 DPI

def get_fonts():
    try:
        return {
            'title': ImageFont.truetype('arialbd.ttf', 72),
            'subtitle': ImageFont.truetype('arialbd.ttf', 40),
            'cat': ImageFont.truetype('arialbd.ttf', 30),
            'item': ImageFont.truetype('arial.ttf', 26),
            'item_bold': ImageFont.truetype('arialbd.ttf', 26),
            'price': ImageFont.truetype('arialbd.ttf', 26),
            'small': ImageFont.truetype('arial.ttf', 22),
            'small_bold': ImageFont.truetype('arialbd.ttf', 22),
            'tiny': ImageFont.truetype('arial.ttf', 18),
        }
    except:
        f = ImageFont.load_default()
        return {k: f for k in ['title','subtitle','cat','item','item_bold','price','small','small_bold','tiny']}

fonts = get_fonts()

# ===== PAGE 1: AFHAALMENU =====
img1 = Image.new('RGB', (W, H), '#FFFFFF')
d1 = ImageDraw.Draw(img1)

y = 80
d1.text((W//2, y), 'Peking Blaricum', fill='#c8102e', font=fonts['title'], anchor='mt')
y += 90
d1.text((W//2, y), 'Chinees Indisch Afhaalrestaurant sinds 1983', fill='#666666', font=fonts['small'], anchor='mt')
y += 60
d1.line([(100, y), (W-100, y)], fill='#c8102e', width=3)
y += 40

# Afhaalmenu A
d1.text((W//2, y), 'Afhaalmenu-A  \u2014  \u20ac 23,50', fill='#c8102e', font=fonts['subtitle'], anchor='mt')
y += 55
d1.text((W//2, y), 'Voor 2 personen met 2 witte rijst', fill='#888888', font=fonts['small'], anchor='mt')
y += 45

menuA = [
    '4 stuks kleine loempia\'s',
    'Sate 2 stokjes',
    'Kroepoek',
    ('Tja Sieuw', 'spec. op Chinese wijze geroosterd varkensvlees met pikante saus'),
    ('Kipfilet in Ketjapsaus', 'kipfilet met zoete pikante saus'),
]
for item in menuA:
    if isinstance(item, tuple):
        d1.text((300, y), '\u2022  ' + item[0], fill='#333333', font=fonts['item_bold'])
        y += 36
        d1.text((340, y), item[1], fill='#888888', font=fonts['tiny'])
        y += 30
    else:
        d1.text((300, y), '\u2022  ' + item, fill='#333333', font=fonts['item'])
        y += 36

y += 20
d1.line([(200, y), (W-200, y)], fill='#DDDDDD', width=1)
y += 40

# Afhaalmenu B
d1.text((W//2, y), 'Afhaalmenu-B  \u2014  \u20ac 23,50', fill='#c8102e', font=fonts['subtitle'], anchor='mt')
y += 55
d1.text((W//2, y), 'Voor 2 personen met 2 witte rijst', fill='#888888', font=fonts['small'], anchor='mt')
y += 45

menuB = [
    '4 stuks kleine loempia\'s',
    'Sate 2 stokjes',
    'Kroepoek',
    ('Babi Pangang', 'geroosterd varkensvlees in pikante saus'),
    ('Foe Yong Hai met kipfilet', 'omelet met kipfilet'),
]
for item in menuB:
    if isinstance(item, tuple):
        d1.text((300, y), '\u2022  ' + item[0], fill='#333333', font=fonts['item_bold'])
        y += 36
        d1.text((340, y), item[1], fill='#888888', font=fonts['tiny'])
        y += 30
    else:
        d1.text((300, y), '\u2022  ' + item, fill='#333333', font=fonts['item'])
        y += 36

y += 30
d1.text((W//2, y), 'Andere gerechten niet mogelijk', fill='#888888', font=fonts['small'], anchor='mt')
y += 50
d1.text((W//2, y), 'i.p.v. witte rijst ook te leveren met:', fill='#666666', font=fonts['small'], anchor='mt')
y += 38
d1.text((W//2, y), 'Nasi of Bami per portie \u20ac 2,00  |  Mihoen of Chinese Bami per portie \u20ac 4,00', fill='#666666', font=fonts['small'], anchor='mt')
y += 70
d1.line([(100, y), (W-100, y)], fill='#c8102e', width=3)
y += 50

# Contact info at bottom
d1.text((W//2, y), 'Wetering 35-39, 1261 ND Blaricum  |  Tel: 035 526 1358', fill='#888888', font=fonts['small'], anchor='mt')
y += 35
d1.text((W//2, y), 'Dagelijks 16:00 - 21:00 (Dinsdag gesloten)', fill='#888888', font=fonts['small'], anchor='mt')

# ===== PAGES 2-3: VOLLEDIGE MENUKAART =====
# Split menu into 2 pages
all_cats = [
    ('Voor- en Bijgerechten', [(1,'Kroepoek',350),(2,'Casava kroepoek',420),(3,'Grote loempia (ham)',520),(4,'Chun Kun (2 stuks)',420),(5,"Kleine Loempia's (8 stuks)",690),(7,'Sate Ajam (kip, 4 stokjes)',780),(8,'Sate Oedang (chin. garnalen, 4 stokjes)',1200),(9,"Chinese Hors d'Oeuvre",800),(10,'Kai Kauw (gefrituurde kippasteitjes 4 st)',620),(11,'Atjar',400),(12,'Tja Tai Ha (4 st gefrituurde garnalen)',1200),(13,'Pisang Goreng (4 st)',420),(14,'Pinda saus',330),(15,'Witte rijst',370),(16,'Patat',370),(17,'Kroket',320),(18,'Frikandel',320)]),
    ('Soepen', [(19,'Kippensoep',450),(20,'Tomatensoep',450),(21,'Haaievinnensoep',450),(23,'Wan Tan soep',650),(24,'Peking soep',600)]),
    ('Nasi Gerechten', [(25,'Nasi Goreng (ei, vlees en ham)',750),(26,'Kleine Nasi Goreng',420),(27,'Nasi Goreng speciaal',1100),(28,'Nasi Goreng Peking',1750),(29,'Nasi Goreng Young Chow',1650),(30,'Nasi Goreng Tjap Wui',1600)]),
    ('Bami Gerechten', [(31,'Bami Goreng (ei, vlees, ham)',750),(32,'Kleine Bami Goreng',420),(33,'Bami Goreng speciaal',1100),(34,'Bami Goreng Peking',1750),(35,'Bami Goreng Tjap Wui',1600)]),
    ('Groente Gerechten', [(37,'Tjap Tjoy met kipfilet',1350),(38,'Tjap Tjoy met ossenhaasfilet',1650),(39,'Tjap Tjoy met chin. grote garnalen',2050),(40,'Tjap Tjoy Peking',1650),(41,'Tjap Tjoy zonder vlees',1150)]),
    ('Eier Gerechten', [(42,'Foe Yong Hai met Tja sieuw',1350),(43,'Foe Yong Hai met ossenhaasfilet',1650),(44,'Foe Yong Hai met kip',1350),(45,'Foe Yong Hai met chin. garnalen',2050),(46,'Foe Yong Hai Peking',1650),(47,'Foe Yong Hai zonder vlees',1150)]),
    ('Mihoen Gerechten', [(48,'Mihoen zonder vlees',1200),(49,'Mihoen Goreng met kipfilet',1380),(50,'Mihoen Goreng met chin. garnalen',1950),(51,'Mihoen Goreng speciaal',1750),(52,'Mihoen Goreng Peking',1900),(53,'Mihoen Goreng Singapore',1680),(54,'Mihoen Goreng klein',800)]),
    ('Vlees Gerechten', [(55,'Babi Pangang',1550),(56,'Szechuan Babi Pangang',1750),(57,'Babi Ketjap',1550),(58,'Koe Loe Yuk',1450)]),
    ('Kip Gerechten', [(61,'Gefileerde kip met cashewnoten',1450),(62,'Gefileerde kip met champignons',1450),(63,'Gefileerde kip met kerrysaus',1450),(64,'Gefileerde kip met babi pangang saus',1450),(65,'Gefileerde kip met ketjap saus',1450),(66,'Gefileerde kip met ananas',1450),(67,'Koe Loe Kai',1450)]),
    ('Ossenhaasfilet', [(68,'Ossenhaasfilet met champignons',1790),(69,'Ossenhaasfilet met kerrysaus',1790),(70,'Ossenhaasfilet met babi pangang saus',1790),(71,'Ossenhaasfilet met ketjap saus',1790)]),
    ('Garnalen Gerechten', [(72,'Garnalen met champignons',2290),(73,'Garnalen met kerrysaus',2290),(74,'Garnalen met babi pangang saus',2290),(75,'Garnalen met paprika',2290),(76,'Koe Loe Ha',2290)]),
    ('Indische Gerechten', [(77,'Nasi Rames Gewoon',1300),(78,'Nasi Rames speciaal',1500),(79,'Bami Rames gewoon',1300),(80,'Bami Rames speciaal',1500),(81,'Gado Gado met rijst (koud)',1150),(82,'Daging Smoor',1600),(83,'Daging Roedjak',1600),(85,'Ajam Pangang Bali',1450),(86,'Ajam Pangang Ketjap',1450),(87,'Ajam Pangang in babi pangang saus',1450)]),
    ('Cantonese Garnalen', [(88,'Tong Koe Ha',2320),(89,'Sin Jir Ha',2320),(90,'Tau Si Ha',2320)]),
    ('Peking Eend', [(94,'Peking Eend',2000),(95,'Tong Koe Eend',2000),(96,'Po Law Eend',1950),(97,'Them Shuen Eend',1950)]),
    ('Cantonese Vlees', [(98,'Tja Sieuw',1700),(99,'Tong Koe Ngauw',1890),(100,'Tau Si Kai',1730),(101,'Tau Si Ngauw',1890),(102,'King Thong Ngauw',2000),(103,'Sin Jir Ngauw',1890)]),
    ('Chinese Bami', [(104,'Chinese bami zonder vlees',1200),(105,'Chinese bami met kipfilet',1380),(106,'Chinese bami met ossenhaasfilet',1680),(107,'Chinese bami met garnalen',1950),(108,'Chinese bami speciaal',1750),(109,'Chinese bami klein',800)]),
    ('Szechuan Gerechten', [(110,'Szechuan Tja Sieuw',1900),(112,'Koen Po Kai',1790),(113,'Koen Po Ngauw',1890),(114,'Koen Po Ha',2350),(116,'Szechuan Laik Kai',1790),(117,'Szechuan Laik Ngauw',1890),(118,'Szechuan Laik Ha',2350),(119,'Szechuan Laik Ab',2200)]),
    ('Combinatie', [(120,'2 gerechten naar keuze',1690)]),
    ('Rijsttafels', [(121,'Indische Rijsttafel 1 persoon',2090),(122,'Indische Rijsttafel 2 personen',4050),(123,'Chinese Rijsttafel 2 personen',4750),(124,'Cantonese Rijsttafel 2 personen',5000)])
]

# Split into 2 pages roughly equal
mid = len(all_cats) // 2
page2_cats = all_cats[:mid]
page3_cats = all_cats[mid:]

def draw_menu_page(d, cats, page_title, start_y=80):
    y = start_y
    d.text((W//2, y), 'Peking Blaricum \u2014 Volledige Menukaart', fill='#c8102e', font=fonts['title'], anchor='mt')
    y += 90
    d.text((W//2, y), page_title, fill='#888888', font=fonts['small'], anchor='mt')
    y += 50
    d.line([(100, y), (W-100, y)], fill='#c8102e', width=2)
    y += 30

    col_w = (W - 200) // 2
    col_x = [100, 100 + col_w + 40]
    col_heights = [0, 0]
    col_cats = [[], []]

    for cat_name, items in cats:
        h = 40 + len(items) * 36 + 15
        shortest = 0 if col_heights[0] <= col_heights[1] else 1
        col_cats[shortest].append((cat_name, items))
        col_heights[shortest] += h

    for col_idx in range(2):
        x = col_x[col_idx]
        cy = y
        for cat_name, items in col_cats[col_idx]:
            # Category header
            d.rectangle([x, cy, x + col_w - 10, cy + 34], fill='#c8102e')
            d.text((x + 10, cy + 4), cat_name.upper(), fill='white', font=fonts['cat'])
            cy += 38
            for num, name, price in items:
                price_str = '\u20ac ' + str(price // 100) + ',' + str(price % 100).zfill(2)
                d.text((x + 5, cy), str(num), fill='#AAAAAA', font=fonts['item'])
                d.text((x + 45, cy), name, fill='#333333', font=fonts['item'])
                d.text((x + col_w - 20, cy), price_str, fill='#c8102e', font=fonts['price'], anchor='rt')
                cy += 36
            cy += 12

    # Footer
    d.line([(100, H - 100), (W - 100, H - 100)], fill='#DDDDDD', width=1)
    d.text((W//2, H - 70), 'In plaats van witte rijst: Nasi of Bami +\u20ac 2,00  |  Mihoen/Chinese Bami +\u20ac 4,00  |  Saus apart +\u20ac 0,50', fill='#888888', font=fonts['small'], anchor='mt')
    d.text((W//2, H - 40), 'Heeft u een allergie? Meld het ons!', fill='#c8102e', font=fonts['small_bold'], anchor='mt')

img2 = Image.new('RGB', (W, H), '#FFFFFF')
d2 = ImageDraw.Draw(img2)
draw_menu_page(d2, page2_cats, 'Gerechten 1 \u2014 Voor-, Soepen, Nasi, Bami, Groenten, Eieren, Mihoen, Vlees, Kip')

img3 = Image.new('RGB', (W, H), '#FFFFFF')
d3 = ImageDraw.Draw(img3)
draw_menu_page(d3, page3_cats, 'Gerechten 2 \u2014 Ossenhaas, Garnalen, Indisch, Cantonese, Eend, Bami, Szechuan, Combinatie, Rijsttafels')

# Save as PDF
output = 'peking-blaricum/menukaart-peking-blaricum.pdf'
img1.save(output, 'PDF', save_all=True, append_images=[img2, img3], resolution=300)
print('PDF created:', os.path.getsize(output), 'bytes')