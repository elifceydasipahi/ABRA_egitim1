# müsteri bilgileri + satin aldigi urun bilgileri
#tolam ödenen ucret?
#odenen miktarin kdv orani? (%18)


musteriAdi= input("isim: ")
musteriTel= input("telefon: ")
musteriAdres= input("adres: ")

musteriBilgileri = musteriAdi + "\n" + musteriTel + "\n" + musteriAdres

kulaklik = 500
mouse = 300
bilgisayar = 5000
kdvOrani = 0.18

alinanUrunler = input("hangi urunleri satin aldiniz? (kulaklik, mouse, bilgisayar):" + "\n")

toplamUcret = 0
if "kulaklik" in alinanUrunler:
    toplamUcret += kulaklik
if "mouse" in alinanUrunler:
    toplamUcret += mouse
if "bilgisayar" in alinanUrunler:
    toplamUcret += bilgisayar

toplamKdv = toplamUcret * kdvOrani
toplamOdenecek = toplamUcret + toplamKdv

print("toplam odenecek ucret: " + str(toplamOdenecek) + " TL")
print("odenen miktarin kdv orani: %" + str(kdvOrani * 100))