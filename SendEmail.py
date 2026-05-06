import smtplib as S

ob = S.SMTP('smtp.gmail.com', 587)
ob.ehlo()
ob.starttls()
ob.login('manmohanmishra535@gmail.com','Ghth@567')
subject = "test python"
body = "I Love Python"
massage = "Subject:{}\n\n{}".format(subject,body)
listadd = ['mishra695@outlook.com',]
ob.sendmail('mishra695@outlook.com', listadd,massage)
print("send mail")
ob.quit()