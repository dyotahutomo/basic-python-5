print ("Selamat Datang!\n")

daftar_kontak = []

# Melihat Daftar Kontak
def kontak ():
    for kontak in daftar_kontak:
        print ("Nama: {}" .format(kontak["nama"]))
        print ("No. Telp: {}" .format(kontak["telepon"]))

# Menambahkan Kontak Baru
def tambah ():
    count = int(input("Jumlah Kontak: "))
    for i in count:
        kontak = {}
        nama_baru = input ("Nama: ")
        telepon_baru = input ("No. Telp: ")
        kontak ["nama"] = nama_baru
        kontak ["telepon"] = telepon_baru
        daftar_kontak.append(kontak)
        print ("Kontak Berhasil Ditambahkan!")

# Keluar dari Program
def keluar ():  
    print  ("Program Selesai, Sampai Jumpa!")

menu = " "
while menu != "3":
    print (
        "--- Menu ---\n"
        "1. Daftar Kontak\n"
        "2. Tambah Kontak\n"
        "3. Keluar\n"
    )
    menu = input("Pilih Menu: ")

    if menu == "1":
        kontak()
    elif menu == "2":
        tambah()
    elif menu == "3":
        keluar()
    else:
        print ("Menu Tidak Tersedia")