
import smtplib, ssl
#  smtplib => E-posta göndermek için arayuz saglar
# ssl => güvenli iletişim sağlar

#  Bu nedenle, ssl kütüphanesi, smtplib kütüphanesiyle birlikte kullanılarak
#  e-postaların güvenli bir şekilde gönderilmesini sağlar.

def send_email(kime,email):
    print("asd ",kime)
    port=465
    smtp_server="example@gmail.com" #! ALICI gmail adres
    sender = "sndr@gmail.com" #! GÖNDEREN gmail adres
    password="" #! kucuk hack ile tek seferlik şif buraya gir

    context= ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server,port,context=context) as smtp:
        smtp.login(sender,password)
        # güvenli şekilde giriş yapıyoruz gönderecek olan kişi email'e
        smtp.sendmail(sender,kime,email)