import json
import time

# Süre ölçme fonksiyonu
def sure_olc(islem, kume):
    baslangic = time.perf_counter()
    sonuc = islem(kume)
    sure = time.perf_counter() - baslangic
    return sonuc, sure


# JSON dosyasını okuma
dosya_adi = input("JSON dosyasının adını giriniz: ")

with open(dosya_adi, "r") as dosya:
    veriler = json.load(dosya)


# Listeleri kümelere dönüştürme
A = set(veriler["A"])
B = set(veriler["B"])

print("A kümesi:", A)
print("B kümesi:", B)


# Küme işlemleri ve süre ölçümü

birlesim, birlesim_suresi = sure_olc(A.union, B)

kesisim, kesisim_suresi = sure_olc(A.intersection, B)

fark_AB, fark_AB_suresi = sure_olc(A.difference, B)

fark_BA, fark_BA_suresi = sure_olc(B.difference, A)


# 5. Sonuçları ekrana yazdırma
nokta = "............................"

print(nokta)
print("Birleşim:", birlesim)
print("Birleşim süresi:", birlesim_suresi)

print(nokta)
print("Kesişim:", kesisim)
print("Kesişim süresi:", kesisim_suresi)

print(nokta)
print("A - B:", fark_AB)
print("A - B süresi:", fark_AB_suresi)

print(nokta)
print("B - A:", fark_BA)
print("B - A süresi:", fark_BA_suresi)


sonuclar = {
    "birlesim": {"sonuc": sorted(birlesim), "sure": birlesim_suresi},
    "kesisim": {"sonuc": sorted(kesisim), "sure": kesisim_suresi},
    "fark_AB": {"sonuc": sorted(fark_AB), "sure": fark_AB_suresi},
    "fark_BA": {"sonuc": sorted(fark_BA), "sure": fark_BA_suresi}
}

with open("sonuclar.json", "w") as dosya:
    json.dump(sonuclar, dosya, indent=4)

print("Sonuçlar dosyaya kaydedildi.")

