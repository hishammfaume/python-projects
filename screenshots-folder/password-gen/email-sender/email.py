import smtplib

to = input("Enter recepient email address: \n")

content = input("Enter email content: \n")

def email(to, content):
    server = smtplib.SMTP("smtp@gmail.com", 587)
    server.ehlo
    server.login("dvdvfou@gmail.com","uiejfiejfe")
    server.starttls
    server.sendmail("senderemail@gmail.com", to, content)
    server.close

email(to, content)