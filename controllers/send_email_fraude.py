import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys

def check_args(args):
    if len(args) != 5:
        print("Error ! \n Usage : send_email_fraude.py [Surname] [Name] [Mail] [Client_ID]")
        sys.exit(1)

check_args(sys.argv)

# ------------- Configuartion SMTP ------------- #

smtp_server = "smtp.gmail.com" 
port = 587  

sender_email = "bankdaddys@gmail.com"  
receiver_email = str(sys.argv[3])   
password = "fmuieqauszmbeoix" 

surname = sys.argv[1]
name = sys.argv[2]
ID = sys.argv[4]

# ------------- Email body ------------- #

msg = MIMEMultipart()
msg["Subject"] = "Insecurity Alert"
msg["From"] = sender_email
msg['To'] = "".join(receiver_email)

text = ""

body_text = MIMEText(text, 'plain')  
msg.attach(body_text) 

html = f"""
<html>
  <body>
    <p style="color:black;"> Dear Sir/Madam {surname} {name}, </p>
    <p style="color:black;">
    I regret to inform you that fraud has been detected on your Bank of Daddys account. <br>
    Don't worry, our team of experts are already working on it! <br>
    For further information, do not hesitate to contact us by providing your customer ID (as a reminder, your ID is the number {int(ID)}). <br>
    Please accept our apologies.
    </p>
    <p style="color:black;">
    Sincerely, Customer Protection Department.
    </p>
    <p style="color:black;">
    <i><strong>28, Avenue Valrose <br>
    06108 Nice Cedex 2 <br>
    Téléphone: 04 89 15 00 00</strong></i>
    </p>
  </body>
</html>
"""

body_html = MIMEText(html, 'html')
msg.attach(body_html)  

# ------------- Send email ------------- #

context = ssl.create_default_context()
# ----------- Try to log in to server ----------- #
try:
    server = smtplib.SMTP(smtp_server, port)
    server.ehlo()  # check connection
    server.starttls(context=context)  # Secure the connection
    server.ehlo()  # check connection
    server.login(sender_email, password)
    # ----------- Send email ----------- #
    server.sendmail(sender_email, receiver_email, msg.as_string())

except Exception as e:
    # ----------- Print any error messages  ----------- #
    print(e)
finally:
    server.quit()
