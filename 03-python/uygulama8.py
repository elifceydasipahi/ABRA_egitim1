#bir aracin yakit tipne göre (benzin, dizel, lpg) belirtilen bir mesafede ne kadar yakit masrafi oldugunu hesaplayan uygulama.


yakitTipi = input("yakit tipini nedir?")
mesafe = float(input("gidilen km: "))

benzin = 39.35
dizel = 41.71
lpg = 20.28

if yakitTipi == "benzin":
    fiyat = benzin

elif yakitTipi == "dizel":
    fiyat = dizel

elif yakitTipi == "lpg":
    fiyat = lpg

else:
    print("bir seyler ters gitti")

topFiyat = fiyat*mesafe
print(topFiyat)