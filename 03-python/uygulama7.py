# bir ögrencinin girilen 3 notuna gore  basari durumunu kontrol et. 70 ve üstü basarili

not1 = float(input("not 1: ")) 
not2 = float(input("not 2: "))
not3 = float(input("not 3: "))

ortalama = (not1 + not2 + not3) / 3 

if ortalama >= 70:
    print("başarılı.")
else:
    print("başarısız.")


#not ortalamasi en az 70 puan ve zayifi yoksa tesekkür belgesi alabilme durumunu kontrol et. zayif not 40 in altindaki notlardir.

if ortalama >= 70:
    if not1 < 40 or not2 < 40 or not3 < 40:
        print("teşekkür belgesi alamazsınız.")
    else:
        print("teşekkür belgesi alabilirsiniz.")


