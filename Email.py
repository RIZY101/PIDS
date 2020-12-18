# Written by Richard Zins for PIDS
import smtplib

server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login("richard.zins447@myci.csuci.edu","Warparty8787!")
msg = 'Subject:PIDS Alert\rPIDS has detected an intrusion! Please check your surveillance dashboard!'
def send():
    file = open('/var/www/html/email.txt', 'r')
    text = file.read()
    server.sendmail("richard.zins447@myci.csuci.edu", text, msg)
