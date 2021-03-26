print ("--- Menu ---")
print ("")
print ("1. Daftar Kontak")
print ("2. Tambah Kontak")
print ("3. Keluar")
print ("")
menu = int(input ("Pilih Menu: "))

if menu == 1:
    daftar_kontak = []
    kontak.append(kontak)
    for i in kontak:
        print ("Nama: {} " .format(nama))
        print ("No. Telp: {} " .format(nomor_telepon))
        break
elif menu == 2:
    count = int(input("Jumlah Data: "))
    nama = []
    nama.append(nama)
    nomor = []
    nomor.append(nomor)

    for i in range (count):
        print ("Data ke {} " .format(i+1))
        nama = input ("Nama: ")
        nomor = int(input("Nomor: "))
    print (nama .format(nama[i]))
    print (nomor)
elif menu == 3:
    print ("Program selesai, sampai jumpa")
else:
    print ("Menu tidak tersedia")

# program masih belum selesai sepenuhnya. Saya bingung