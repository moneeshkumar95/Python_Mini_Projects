"""
A SIMPLE EMAIL SENDER USING SMTP
"""
import smtplib
from email.message import EmailMessage


def sender():
    sender_mail = input("Please enter the sender mail I'd: ")
    sender_password = input("Please enter the sender password: ")
    to_email = input("Please enter the to mail I'd: ")
    subject = input("Please enter the subject: ")
    body = input("Please enter the body: ")

    email_data = EmailMessage()
    email_data['From'] = sender_mail
    email_data['To'] = to_email
    email_data['Subject'] = subject
    email_data.set_content(body)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(sender_mail, sender_password)
        server.sendmail(sender_mail, to_email, email_data.as_string())
        return 'Email sent successfully'


if __name__ == '__main__':
    print(sender())
