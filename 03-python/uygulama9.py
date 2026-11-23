urunler = [
    {"urunAdi":"Hp Victus", "fiyat": 32999},
    {"urunAdi":"Lenovo ThinkPad", "fiyat": 25499},
    {"urunAdi":"Apple Macbook", "fiyat": 49999},
    {"urunAdi":"Huawei Matebook", "fiyat": 26999},
    {"urunAdi":"Casper Nirvana", "fiyat": 20000}
]


# 1- Aşağıdaki örnek cümleyi tüm ürünlere uygulayınız.
#    "Hp Victus marka ürünün fiyatı 32999 Türk Lirası."

for urun in urunler:
    print(f"{urun['urunAdi']} marka ürün fiyatı {urun['fiyat']} Türk Lirası.")

# 2- Ürünlerin fiyatları toplamı nedir?

toplam = 0
for urun in urunler:
    toplam += urun["fiyat"]
print (toplam)


# 3- 25000 ile 40000 arasındaki ürünleri listeleyiniz.

for urun in urunler:
    if urun["fiyat"] >= 25000 and urun["fiyat"] <= 40000:
        print(urun["urunAdi"])

# 4- Kullanıcıdan alınan anahtar kelimeye göre ürünlerin fiyatini listeleyiniz.

kelime = input("kelime: ")

for urun in urunler:
    if kelime in urun["urunAdi"]:
        print(urun["fiyat"])