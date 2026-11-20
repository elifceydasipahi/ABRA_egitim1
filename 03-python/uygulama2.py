# yari capi verilen dairenin alanini hesapla
# girilen km bilgisini mil cinsinde hesapla

import math

yariCap = float(input("yari capi girin: "))
alan = math.pi * yariCap ** 2
print("dairenin alani: " + str(alan))

km = float(input("km girin: "))
mil = km / 1.609
print("mil: " + str(mil))