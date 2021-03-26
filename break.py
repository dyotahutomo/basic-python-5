# for i in range(6):
#     if i == 3:
#         break
#     print(i)

# text = input("Masukkan text: ")
# while True:
#     if text == "stop" or text == "end":
#         break
#     print("text: {}" .format(text))
#     text = input("Masukkan text: ")

count = 0
threshold = 3
user = "dyotahutomo@gmail.com"
password = "12345"

while True:
    if count == threshold:
        print ("Percobaan login melewati batas!")
        break
    user_name = input ("Masukkan username anda: ")
    user_pass = input ("Masukkan password anda: ")
    count += 1
    if user_name == user and user_pass == password:
        print ("Login berhasil!")
        break
    else:
        print ("Username dan Password anda salah!")