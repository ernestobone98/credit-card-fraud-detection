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
msg["Subject"] = "Alerte d'insécurité"
msg["From"] = sender_email
msg['To'] = "".join(receiver_email)

text = ""

body_text = MIMEText(text, 'plain')  
msg.attach(body_text) 

html = f"""
<html>
  <body>
    <p style="color:black;"> Bonjour Madame, Monsieur {surname} {name}, </p>
    <p style="color:black;">
    Nous vous informons qu'une fraude a été détectée sur votre compte Bank of Daddys. <br>
    Rassurez-vous, notre équipe d'experts y travaille déjà ! <br>
    Nous sommes à votre disposition pour toutes informations complémentaires, 
    n'hésitez pas à nous contacter en nous fournissant votre identifiant client (pour rappel, votre identifiant est le n°{int(ID)}).
    </p>
    <p style="color:black;">
    Bien cordialement, le Département Protection Clients.
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
# Try to log in to server and send email 
try:
    server = smtplib.SMTP(smtp_server, port)
    server.ehlo()  # check connection
    server.starttls(context=context)  # Secure the connection
    server.ehlo()  # check connection
    server.login(sender_email, password)

    # Send email here
    server.sendmail(sender_email, receiver_email, msg.as_string())

except Exception as e:
    # Print any error messages 
    print(e)
finally:
    server.quit()