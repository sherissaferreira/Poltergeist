import smtplib
server = smtplib.SMTP("smtp.gmail.com",587)
server.ehlo()
server.startttls()

username = "sferreira6066@baysidehighschool.org"
password = "219626066"

server.login(username,password)
server.sendmail(username,"username","Hey!")
