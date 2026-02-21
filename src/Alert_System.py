import smtplib
from email.mime.text import MIMEText

def send_email_alert(value):
    msg = MIMEText(f"Warning, Poor air quality detector.\nGas Value : {value}")
    msg['Subject'] = "Alert"
    msg['From'] = "email@gmail.com"
    msg['To'] = "recipient@gmail.com"

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(msg['From'], msg['To'])
        server.send_message(msg)