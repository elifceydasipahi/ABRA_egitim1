customers = ["elifceyda", "eda", "ayse", "fatma"]
order_totals = [12000, 15000, 10000, 20000]

#elifceyda kullanici adliyla yapilan  15000 tl lik siparisi listeye ekle
customers.append("elifceyda")
order_totals.append(15000)
print(customers)

#son eklenen siparisi sil
customers.pop()
order_totals.pop()

#tüm siparisler icin "<username> kullanicisinin siparisi <siparis tutari> tl" seklinde yazdir
for i in range(len(customers)):
    print(f"{customers[i]} kullanicisinin siparisi {order_totals[i]} tl")

#müsterileri alfabetik olarak sirala ve yazdir
customers.sort()
print(customers)

#siparis toplamlarini azalan seklinde sirala ve yazdir
order_totals.sort
order_totals.reverse()
print(order_totals)

#en düsük siparis tutarini yazdir
print(min(order_totals))
print(max(order_totals))

#elifceyda adli kullanicinin kac siparisi oldugunu yazdir
print(customers.count("elifceyda"))

#costomer listesinden eda kullanicisini sil
customers.remove("eda")

#listelerdeki tum icerikleri sil
customers.clear()
order_totals.clear()

#kullanicidan alinan kullanici adi ve siparis tutarini listelere ekle
username = input("Kullanici adi giriniz: ")
order_total = int(input("Siparis tutarini giriniz: "))
customers.append(username)
order_totals.append(order_total)