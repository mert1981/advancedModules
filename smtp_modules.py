import smtplib #smtp serverine bağlanmamız için bu modulü dahil ettik 
from email.mime.multipart import MIMEMultipart #mail yapısını oluşturcak
from email.mime.text import MIMEText # mesaj gövdemizi yani mailimize ne yazıcaz onu yazıyoruz
import sys 

mesaj = MIMEMultipart() #mail yapısı oluşturuyoruz

mesaj["From"] = "mertkoc1981@gmail.com" # mail kimden gelecek
mesaj["To"] = "cetin.yazici2525@gmail.com" # mail kime gidecek
mesaj["Subject"] = "SMTP ile mail gönderme" # mailin konusu 
yazi = """
Python ile kod yazarak mail gönderiyorum.
Mert Koç

"""
mesaj_govdesi = MIMEText(yazi,"plain") #plain yazarak normal bir yazı göndereceğimizi söylüyoruz
mesaj.attach(mesaj_govdesi)

try:
    mail = smtplib.SMTP("smtp.gmail.com",587)
    mail.ehlo() 
    mail.starttls()
    mail.login("mertkoc1981@gmail.com","mert.1981-23")
    mail.sendmail(mesaj["From"],mesaj["To"],mesaj.as_string())
    print("mail başarıyla gönderildi...")
    mail.close()
except:
    sys.stderr.write("Bir sorun oluştu.")
    sys.stderr.flush()