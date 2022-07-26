# PROGRAM PENYEWAAN PENGINAPAN
# TUGAS BESAR ALPRO
# ANGGOTA:
# 1. ALFIAN PUTRA LAKSANA BINTANG -- 1102210019 -- CE 04-01
# 2. ISYA' SYECHAN FAEDILLAH      -- 1102210001 -- CE 04-01
#-----------------------------------------------------------------

strip="--------------------------"
strippanjang="----------------------------------------------------"
def main():
    print("\nHotel Teknik Komputer")
    print(strip)
    print("SELAMAT DATANG DI HOTEL TEKNIK KOMPUTER")
    print("SILAHKAN PILIH MENU DIBAWAH INI")
    print(strip)
main()

def menu():
    print("MASUKAN PILIHAN DALAM ANGKA", "\n    KECUALI KODE KAMAR")
    print("\n1. Informasi Kamar", "\n2. Harga Kamar", "\n3. Pemesanan", "\n4. Cari Pesanan Anda", "\n5. Daftar Pesanan", "\n0. Keluar")    
menu()

choice = int(input("\nMasukan Pilihan (Angka): "))
while choice != 0:
    if choice == 1:
        print()
        print(strip)
        print("INFORMASI KAMAR")
        print(strip)
        print("Single = Single bed, AC, WI-FI, TV,")
        print('Double = Double bed, AC, WI-FI, TV, Free breakfast untuk 2 orang')
        print("Deluxe = Double bed, Ruangan lebih luas, Sofa, AC, WI-FI, TV, Free breakfast untuk 4 orang ")
        print(strippanjang)
    
    
    elif choice == 2:
        print("\nHotel Teknik Komputer")
        print(strip)
        print("Jenis    Kode       Harga")
        print(" ")
        print("Single    S      Rp. 200.000")
        print("Double    D      Rp. 325.000")
        print("Deluxe    DX     Rp. 550.000")
        print(strip)

    elif choice == 3:
        user = input('Nama : ')
        print("Jenis    Kode       Harga")
        print(" ")
        print("Single    S      Rp. 200.000")
        print("Double    D      Rp. 325.000")
        print("Deluxe    DX     Rp. 550.000")
        data = int(input("\nSewa berapa jenis kamar? = "))
        print("\nPesan untuk tanggal berapa?")
        print("   MASUKAN DALAM ANGKA")
        tanggal = int(input("\nTanggal: "))
        bulan = int(input("Bulan: "))
        tahun = int(input("Tahun: "))
        waktu = tanggal, bulan, tahun

        listKK = []
        listLI = []
        
        #Input
        for x in range(data):
            print(strip)
            print("\nKamar ke -",x+1)
            kdk = input("Masukan Kode jenis kamar = ")
            listKK.append(kdk)
            mlm = int(input("Lama inap (Malam) = "))
            listLI.append(mlm)
            print(strip)

        #Output
        print("Nama Customer : ",user)
        print(strip)
        print("Hotel Teknik Komputer")
        print(strippanjang)
        print("No.    Jenis     Harga         Lama Inap       Harga")
        print("       Kamar     Permalam       (Malam)                ")
        print(strippanjang)

        tot=0
        for a in range (data):
            if(listKK[a]=="s" or listKK[a]=="S"):
                kamar = "Single"
                harga = 200000
            elif(listKK[a]=="d" or listKK[a]=="D"):
                kamar = "Double"
                harga = 325000
            elif(listKK[a]=="dx" or listKK[a]=="DX"):
                kamar = "Deluxe"
                harga = 550000
            subtot = harga * listLI[a]
            tot = tot+subtot
            print(a+1, "   ", kamar ,"   Rp", harga ,"       ", listLI[a] ,"       Rp", subtot   )
            print(strippanjang)

        print("KONFIRMASI PESANAN", "\n1. Batalkan pesanan", "\n2. Lanjutkan")
        konfirmasi = int(input("\nMasukan Pilihan = "))
        if konfirmasi == 2:
            print("Dipesanan untuk tanggal :",waktu)
            print("Nama Customer : ",user)
            print(strip)
            print("Hotel Teknik Komputer")
            print(strippanjang)
            print("No.    Jenis     Harga         Lama Inap       Harga")
            print("       Kamar     Permalam       (Malam)                ")
            print(strippanjang)
            tot=0
            for a in range (data):
                if(listKK[a]=="s" or listKK[a]=="S"):
                    kamar = "Single"
                    harga = 200000
                elif(listKK[a]=="d" or listKK[a]=="D"):
                    kamar = "Double"
                    harga = 325000
                elif(listKK[a]=="dx" or listKK[a]=="DX"):
                    kamar = "Deluxe"
                    harga = 550000
                subtot = harga * listLI[a]
                tot = tot+subtot
                print(a+1, "   ", kamar ,"   Rp", harga ,"       ", listLI[a] ,"       Rp", subtot   )
                print(strippanjang)
                file = open('data.txt','a')
                file.write("\n")
                file.write(user)
                file.write("*")
                file.write(kamar)
                file.write("*")
                file.write(str(listLI[a]))
                file.write("*")
                file.write(str(harga))
                file.write("*")
                file.write(str(waktu))
                file.write("*")
            file.write(str(tot))
            file.close()
            print("                           ","Total Bayar = Rp.", int(tot))
            

        elif konfirmasi == 1:
            print("\n  **Pesanan Dibatalkan**")
       
    elif choice == 4:
        print("\n     RIWAYAT PEMESANAN")
        print(strip)
        file = open('data.txt','r')
        nama = input("Masukan Nama Pemesan: ")
        for i in file:
            i = i.replace("\n", "")
            data_split = (i.split("*"))
            if data_split[0]== nama:
                print(strippanjang)
                print("Data berhasil ditemukan!")
                print("Nama          : ", data_split[0])
                print("Kode Kamar    : ", data_split[1])
                print("Lama Inap     : ", data_split[2])
                print("Harga         : ", data_split[3])
                print("Dipesan untuk : ", data_split[4])
        file.close()
        
        print(strippanjang)

    elif choice == 5:
        # Read
        daftar = []
        file = open("data.txt", 'r')
        for i in file:
            i = i.replace("\n", " ")
            daftar.append(i.strip())
        file.close()

        # Sorting
        daftar.sort()

        # Data sorted
        filename = "data_sorted.txt"
        with open(filename, "w") as fileout:
            for a in daftar:
                fileout.write(a +'\n')

        # Output
        print("\n       Data Pesanan  ")
        print("        Yang Masuk   ")
        print(strip)
        file = open('data_sorted.txt','r')
        for d in file:
            d = d.replace("\n", "")
            data_split = (d.split("*"))
            print("Nama          : ", data_split[0])
            print("Kode Kamar    : ", data_split[1])
            print("Lama Inap     : ", data_split[2])
            print("Harga         : ", data_split[3])
            print("Dipesan untuk : ", data_split[4])
            print(" ")
        file.close()
        
    else: 
        print("\n     *INVALID INPUT*")
        print(" ")
        print(strip)
        
    menu()
    choice = int(input("\nMasukan Pilihan (Angka)= "))

print('Terima Kasih')