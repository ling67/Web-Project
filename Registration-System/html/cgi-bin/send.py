#!/usr/local/bin/python3

# Jackie Chan sends email to Bruce Lee
import smtplib

def sendEmailToUser(userEmail, msg):
    with open('/Users/linda/Documents/pw.txt') as file:
        data = file.readlines()

    gmail_user = '123dearling@gmail.com'
    gmail_password = data[0]

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    # The sender Jackie Chan needs to log in to
    # the mail server.
    server.login(gmail_user, gmail_password)

    # To send this email using gmail, Bruce Lee needs to turn on
    # "Less secure apps" in his gmail account to be able to receive
    # less secure email from Jackie Chan.
    #      https://myaccount.google.com/lesssecureapps
    server.sendmail(gmail_user, userEmail, msg)
    server.quit()