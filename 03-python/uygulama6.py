a, b, c = 4, 8, (12, 2)

#kullanicidan alinan 2 sayinin carpimi ile a,b,c toplaninin farki nedir

sayi1 = int(input("sayi1: ")) 
sayi2 = int(input("sayi2: ")) 
carpim = sayi1 * sayi2
toplam = a + b + sum(c)
fark = carpim - toplam
print(f"Fark: {fark}")

#c nin tolamlarinin b ye kalansiz bölümü nedir
bölum = sum(c) // b
print(f"Bölüm: {bölum}")

# a b c toplamlarinin mod 7 si ne
mod = (a + b + sum(c)) % 7
print(f"Mod 7: {mod}")

#b nin a. kuvvetini hesalpla
kuvvet = b ** a
print(f"kuvveti: {kuvvet}")

# a, b, *c = (2,4,6,8,13) islemine göre c in degerlerinin toplami nedir
print(sum(c))