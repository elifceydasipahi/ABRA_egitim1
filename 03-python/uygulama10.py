# 1- Kendisine gönderilen bir kelimeyi belirtilen kez ekranda gösteren fonksiyonu yazınız.

def yazdir(text, adet):
    return text * adet

print(yazdir("Merhaba", 5))


# 2- Dikdörtgenin alan ve çevresini hesaplayan fonksiyonu yazınız.

def hesapla(kisa, uzun):
    alan = kisa * uzun
    cevre = 2 * (kisa + uzun)
    return alan, cevre

print(hesapla(5, 10))
# 3- Yazı tura uygulamasını fonksiyon kullanarak yapınız. (Random modülü)

def yaziTura():
    import random
    sayi = random.random()

    if sayi > 0.5:
        return "tura"
    else:
        return "yazi"


# 4- Kendisine gönderilen 2 sayı arasındaki tüm asal sayıları bulan fonksiyonu yazınız.

def asal_sayilar(baslangic, bitis):
    for sayi in range(baslangic, bitis + 1):
        if sayi > 1:
            for i in range(2, sayi):
                if sayi % i == 0:
                    break
            else:
                print(sayi)

asal_sayilar(10, 30)

# 5- Kendisine gönderilen bir sayının tam bölenlerini bir liste şeklinde döndüren fonksiyonu yazınız.

def bolenler(sayi):
    liste = []

    for i in range(1, sayi + 1):
        if sayi % i == 0:
            liste.append(i)

    return liste

print(bolenler(20))