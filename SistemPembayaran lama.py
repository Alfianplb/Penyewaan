# ALFIAN PUTRA LAKSANA BINTANG
# NIM 1102210019 CE 04-01
# PEMBAYARAN PENGINAPAN HOTEL

strip="--------------------------"
strippanjang="----------------------------------------------------"
print("Hotel Teknik Komputer")
print(strip)
print("Jenis    Kode       Harga")
print(" ")
print("Single    S      Rp. 200.000")
print("Double    D      Rp. 325.000")
print("Deluxe    DX     Rp. 550.000")
print(strip)
data = int(input("\nSewa berapa jenis kamar? = "))

#deklarasi variabel list
listKK = []
listBK = []

#input
for x in range(data):
    kdk = input("Masukan Kode jenis kamar = ")
    listKK.append(kdk)
    bkk = int(input("Lama inap (Malam) = "))
    listBK.append(bkk)
    print(strip)

#output
print(strip)
print("Hotel Teknik Komputer")
print(strippanjang)
print("No.    Jenis     Harga      Lama Inap    Total Harga")
print("       Kamar     Permalam    (Malam)                ")
print(strippanjang)

#perulangan
tot=0
for a in range (data):
    if(listKK[a]=="s" or listKK[a]=="S"):
        jk="Single"
        harga = 200000
    elif(listKK[a]=="d" or listKK[a]=="d"):
        jk="Double"
        harga = 325000
    elif(listKK[a]=="dx" or listKK[a]=="DX"):
        jk="Deluxe"
        harga = 550000
    subtot = harga * listBK[a]
    tot = tot+subtot
    print(a+1, "   ", jk ,"   ", harga ,"       ", listBK[a] ,"        Rp.", subtot   )
    print(strippanjang)


print("                           ","Total Bayar = Rp.", int(tot))
