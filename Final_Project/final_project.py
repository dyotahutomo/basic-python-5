# https://www.pythonindo.com/cara-mengirim-email-menggunakan-python/

# smtp adalah simple mail transfer protocol
# digunakan untuk berkomunikasi dengan server untuk mengirimkan email ke server, kemudian dikirim ke server penerima
# sumber : niagahoster.co.id
import smtplib
# MIME adalah multipurpose internet mail extention
# digunakan untuk menginzinkan data selain text agar dapat di transfer lewat email tanpa translate ke format ASCII
# sumber : wikipedia.com
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

fromaddr = "DYOTAHUTOMO@GMAIL.COM"
toaddr = "BIRAYA98@GMAIL.COM, DYOTAHUTOMO@GMAIL.COM"
msg = MIMEMultipart ()
msg ['From'] = fromaddr
msg ['To'] = toaddr
msg ['Subject'] = "DIKIRIM LEWAT PYHTON"

body = "ada isinya gak nih?"
msg.attach (MIMEText(body,'plain'))

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls ()
server.login (fromaddr, "dyota118787")
text = msg.as_string()
server.sendmail (fromaddr, toaddr, text)
server.quit