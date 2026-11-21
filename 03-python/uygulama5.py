# ögrenci bilgilerini dictiorary listesinde sakla

ögrenciler = {
    101: { 
        "isim": "ayse",
        "dtt": 2010,
        "puan": [85, 90, 78] } ,

    102: {
        "isim": "ali",
        "dtt": 2011,
        "puan": [88, 92, 80] },

    103: {
        "isim": "mehmet",
        "dtt": 2010,
        "puan": [75, 85, 95] }
}

#girilen ögrenci numaraasina göre ögrenci bilgilerini ekrana yazdır

ogrenci_no = int(input("Ögrenci numarasını giriniz: "))
if ogrenci_no in ögrenciler:
    ögrenci = ögrenciler[ogrenci_no]
    print(f"Ögrenci İsmi: {ögrenci['isim']}")
    print(f"Doğum Tarihi: {ögrenci['dtt']}")
    print(f"Puanlar: {ögrenci['puan']}")

else:
    print("Ögrenci bulunamadı.")