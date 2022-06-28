# PEMBAYARAN PENGINAPAN HOTEL

strip="--------------------------"
strippanjang="----------------------------------------------------"
while(True):
    print("\nHotel Teknik Komputer")
    print(strip)
    print("Jenis    Kode       Harga")
    print(" ")
    print("Single    S      Rp. 200.000")
    print("Double    D      Rp. 325.000")
    print("Deluxe    DX     Rp. 550.000")
    print(strip)
    print("1. Informasi Kamar", "\n2. Pemesanan", "\n3. Keluar",)
    print("***MASUKAN PILIHAN DALAM ANGKA***", "\n       KECUALI KODE KAMAR")
    choice1 = int(input("\nMasukan Pilihan (Angka)= "))
    if choice1 == 1:
        print(strippanjang)
        print("INFORMASI KAMAR")
        print(strip)
        print("Single = Single bed, AC, WI-FI, TV,")
        print('Double = Double bed, AC, WI-FI, TV, Free breakfast untuk 2 orang')
        print("Deluxe = Double bed, Ruangan lebih luas, Sofa, AC, WI-FI, TV, Free breakfast untuk 4 orang ")
        print(strip)
        print("1. Kembali", "\n2. Keluar")
        choiceinfo = int(input("\nMasukan Pilihan = "))
        if choiceinfo == 2:
            print('\n    --- Terima Kasih ---')
            break
    elif choice1 == 2:
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
        print("No.    Jenis     Harga      Lama Inap         Harga")
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
        break

    elif choice1 == 3:
        print('\n    --- Terima Kasih ---')
        break
        
    

    

