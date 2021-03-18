x = input ("Masukkan nilai ujian teori: ")
y = input ("Masukkan nilai ujian praktek: ")
a = float(x)
b = float (y)

if a >= 70 and b >= 70:
   print ("Selamat, anda lulus")
elif a >= 70 and b < 70:
    print ("Anda harus mengulang ujian praktek")
elif a < 70 and b >= 70:
    print ("Anda harus mengulang ujian teori")
else:
    print ("Anda harus mengulang ujian teori dan praktek")           