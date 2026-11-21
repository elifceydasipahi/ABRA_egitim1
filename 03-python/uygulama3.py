markalar = ["Toyota", "Honda", "Ford", "BMW", "Mercedes"]

print("test basladi")

#liste kac elemanli
print(len(markalar))

#listenin ilk ve  son elemanini yazdir
print(markalar[0])
print(markalar[-1])

#"toyota" markasini "togg" ile guncelle
markalar[0] = "togg" 
print(markalar)

#tog listenin icinde mi?
if "togg" in markalar:
    print("togg listede var")

elif "togg" not in markalar:
    print("togg listede yok")

#listenin ilk iki  elemanini yazdir
print(markalar[0:2])

#listenin sonuna "audi" ve "nissan" markalarini ekle
markalar.append("audi") 
markalar.append("nissan")
print(markalar)

#listenin son elemanini sil
del markalar[-1]
print(markalar)

#asagidaki verileri liste icerisinde sakla
#ögrenci1: yigit bilgi 2010 [70,80,90]
#ögrenci2: ayse bilgi 2011 [80,90,100] 
#ogrenci3: mehmet bilgi 2012 [60,70,80]

ogrenci1 = ["yigit", "bilgi", 2010, [70, 80, 90]]
ogrenci2 = ["ayse", "bilgi", 2011, [80, 90, 100]]
ogrenci3 = ["mehmet", "bilgi", 2012, [60, 70, 80]]

#ögrenci yaslarini hesapla ve yazdir
ogrenci1Yas = 2026 - ogrenci1[2]
ogrenci2Yas = 2026 - ogrenci2[2]
ogrenci3Yas = 2026 - ogrenci3[2]
print("ogrenci1 yasi: " + str(ogrenci1Yas))
print("ogrenci2 yasi: " + str(ogrenci2Yas))
print("ogrenci3 yasi: " + str(ogrenci3Yas))

#ogrencilerin not ortalamalarini hesapla ve yazdir
ogrenci1NotOrt = sum(ogrenci1[3]) / len(ogrenci1[3])
ogrenci2NotOrt = sum(ogrenci2[3]) / len(ogrenci2[3])
ogrenci3NotOrt = sum(ogrenci3[3]) / len(ogrenci3[3])
print("ogrenci1 not ortalamasi: " + str(ogrenci1NotOrt))
print("ogrenci2 not ortalamasi: " + str(ogrenci2NotOrt))
print("ogrenci3 not ortalamasi: " + str(ogrenci3NotOrt))