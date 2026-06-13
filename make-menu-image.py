from PIL import Image, ImageDraw, ImageFont
import os

# Full-menu overview image: 1920x1080, readable in one glance
W, H = 1920, 1080
img = Image.new('RGB', (W, H), '#FFFFFF')
d = ImageDraw.Draw(img)

# Fonts
try:
    title = ImageFont.truetype('arialbd.ttf', 42)
    subtitle = ImageFont.truetype('arial.ttf', 18)
    cat = ImageFont.truetype('arialbd.ttf', 16)
    item = ImageFont.truetype('arial.ttf', 14)
    price = ImageFont.truetype('arialbd.ttf', 14)
    small = ImageFont.truetype('arial.ttf', 13)
except Exception:
    title = ImageFont.load_default()
    subtitle = title
    cat = title
    item = title
    price = title
    small = title

# Header
d.text((W//2, 22), 'Peking Blaricum - Volledige menukaart', fill='#c8102e', font=title, anchor='mt')
d.text((W//2, 72), 'Meeneem-prijslijst november 2025 - Chinees / Indisch Restaurant', fill='#666666', font=subtitle, anchor='mt')

# Afhaalmenu quick overview
y = 105
left = 120
right = 1050
box_h = 115
d.rectangle([80, y, 900, y+box_h], outline='#c8102e', width=2, fill='#fff8f0')
d.rectangle([1020, y, 1840, y+box_h], outline='#c8102e', width=2, fill='#fff8f0')
d.text((490, y+18), 'Afhaalmenu-A  € 23,50', fill='#c8102e', font=cat, anchor='mt')
d.text((490, y+50), '4 stuks kleine loempia\'s  |  Sate 2 stokjes  |  Kroepoek', fill='#333333', font=small, anchor='mt')
d.text((490, y+78), 'Tja Sieuw  |  Kipfilet in Ketjapsaus', fill='#333333', font=small, anchor='mt')
d.text((1430, y+18), 'Afhaalmenu-B  € 23,50', fill='#c8102e', font=cat, anchor='mt')
d.text((1430, y+50), '4 stuks kleine loempia\'s  |  Sate 2 stokjes  |  Kroepoek', fill='#333333', font=small, anchor='mt')
d.text((1430, y+78), 'Babi Pangang  |  Foe Yong Hai met kipfilet', fill='#333333', font=small, anchor='mt')

# Menu categories and items
cats = [
    ('Voor- en Bijgerechten', [(1,'Kroepoek',350),(2,'Casava kroepoek',420),(3,'Grote loempia',520),(4,'Chun Kun 2st',420),(5,"Kleine loempia 8st",690),(7,'Sate Ajam 4st',780),(8,'Sate Oedang 4st',1200),(9,"Chinese Hors d'Oeuvre",800),(10,'Kai Kauw 4st',620),(11,'Atjar',400),(12,'Tja Tai Ha 4st',1200),(13,'Pisang Goreng 4st',420),(14,'Pinda saus',330),(15,'Witte rijst',370),(16,'Patat',370),(17,'Kroket',320),(18,'Frikandel',320)]),
    ('Soepen', [(19,'Kippensoep',450),(20,'Tomatensoep',450),(21,'Haaievinnensoep',450),(23,'Wan Tan soep',650),(24,'Peking soep',600)]),
    ('Nasi', [(25,'Nasi Goreng',750),(26,'Kleine Nasi',420),(27,'Nasi speciaal',1100),(28,'Nasi Peking',1750),(29,'Nasi Young Chow',1650),(30,'Nasi Tjap Wui',1600)]),
    ('Bami', [(31,'Bami Goreng',750),(32,'Kleine Bami',420),(33,'Bami speciaal',1100),(34,'Bami Peking',1750),(35,'Bami Tjap Wui',1600)]),
    ('Groenten + rijst', [(37,'Tjap Tjoy kip',1350),(38,'Tjap Tjoy ossenhaas',1650),(39,'Tjap Tjoy garnalen',2050),(40,'Tjap Tjoy Peking',1650),(41,'Tjap Tjoy zonder',1150)]),
    ('Eieren + rijst', [(42,'Foe Yong Tja sieuw',1350),(43,'Foe Yong ossenhaas',1650),(44,'Foe Yong kip',1350),(45,'Foe Yong garnalen',2050),(46,'Foe Yong Peking',1650),(47,'Foe Yong zonder',1150)]),
    ('Mihoen', [(48,'Mihoen zonder',1200),(49,'Mihoen kipfilet',1380),(50,'Mihoen garnalen',1950),(51,'Mihoen speciaal',1750),(52,'Mihoen Peking',1900),(53,'Mihoen Singapore',1680),(54,'Mihoen klein',800)]),
    ('Vlees + rijst', [(55,'Babi Pangang',1550),(56,'Szechuan Babi',1750),(57,'Babi Ketjap',1550),(58,'Koe Loe Yuk',1450)]),
    ('Kip + rijst', [(61,'Kip cashewnoten',1450),(62,'Kip champignons',1450),(63,'Kip kerry',1450),(64,'Kip babi pangang',1450),(65,'Kip ketjap',1450),(66,'Kip ananas',1450),(67,'Koe Loe Kai',1450)]),
    ('Ossenhaas + rijst', [(68,'Ossenhaas champ.',1790),(69,'Ossenhaas kerry',1790),(70,'Ossenhaas babi',1790),(71,'Ossenhaas ketjap',1790)]),
    ('Garnalen + rijst', [(72,'Garnalen champ.',2290),(73,'Garnalen kerry',2290),(74,'Garnalen babi',2290),(75,'Garnalen paprika',2290),(76,'Koe Loe Ha',2290)]),
    ('Indisch', [(77,'Nasi Rames gewoon',1300),(78,'Nasi Rames spec.',1500),(79,'Bami Rames gewoon',1300),(80,'Bami Rames spec.',1500),(81,'Gado Gado',1150),(82,'Daging Smoor',1600),(83,'Daging Roedjak',1600),(85,'Ajam Pangang Bali',1450),(86,'Ajam Kecap',1450),(87,'Ajam babi pangang',1450)]),
    ('Cant. Garnalen', [(88,'Tong Koe Ha',2320),(89,'Sin Jir Ha',2320),(90,'Tau Si Ha',2320)]),
    ('Peking Eend', [(94,'Peking Eend',2000),(95,'Tong Koe Eend',2000),(96,'Po Law Eend',1950),(97,'Them Shuen Eend',1950)]),
    ('Cant. Vlees', [(98,'Tja Sieuw',1700),(99,'Tong Koe Ngauw',1890),(100,'Tau Si Kai',1730),(101,'Tau Si Ngauw',1890),(102,'King Thong Ngauw',2000),(103,'Sin Jir Ngauw',1890)]),
    ('Chinese Bami', [(104,'Bami zonder',1200),(105,'Bami kipfilet',1380),(106,'Bami ossenhaas',1680),(107,'Bami garnalen',1950),(108,'Bami speciaal',1750),(109,'Bami klein',800)]),
    ('Szechuan', [(110,'Szechuan Tja Sieuw',1900),(112,'Koen Po Kai',1790),(113,'Koen Po Ngauw',1890),(114,'Koen Po Ha',2350),(116,'Szechuan Laik Kai',1790),(117,'Szechuan Laik N.',1890),(118,'Szechuan Laik Ha',2350),(119,'Szechuan Laik Ab',2200)]),
    ('Combinatie', [(120,'2 naar keuze',1690)]),
    ('Rijsttafels', [(121,'Indische 1p',2090),(122,'Indische 2p',4050),(123,'Chinese 2p',4750),(124,'Cantonese 2p',5000)])
]

# Balance categories over 6 columns by height
col_w = (W - 80) // 6
col_x = [40 + i * col_w for i in range(6)]
col_heights = [0] * 6
col_items = [[] for _ in range(6)]

for cat_name, items in cats:
    h = 30 + len(items) * 19 + 10
    idx = col_heights.index(min(col_heights))
    col_items[idx].append((cat_name, items))
    col_heights[idx] += h

# Draw columns
for ci in range(6):
    x = col_x[ci]
    y = 255
    for cat_name, items in col_items[ci]:
        cw = col_w - 8
        d.rectangle([x, y, x+cw, y+24], fill='#c8102e')
        d.text((x+4, y+3), cat_name.upper(), fill='white', font=cat)
        y += 26
        for num, name, price_cents in items:
            p = f"€ {price_cents//100},{price_cents%100:02d}"
            d.text((x+2, y), str(num), fill='#999999', font=item)
            d.text((x+28, y), name, fill='#333333', font=item)
            d.text((x+cw-4, y), p, fill='#c8102e', font=price, anchor='rt')
            y += 19
        y += 8

# Footer
d.line([(80, H-42), (W-80, H-42)], fill='#dddddd', width=1)
d.text((W//2, H-18), 'Nasi/Bami +€ 2,00  |  Mihoen/Chinese Bami +€ 4,00  |  Saus apart +€ 0,50', fill='#666666', font=small, anchor='mt')

out = 'peking-blaricum/menukaart-afbeelding.png'
img.save(out, 'PNG', optimize=True)
print('Created:', out, os.path.getsize(out), 'bytes')