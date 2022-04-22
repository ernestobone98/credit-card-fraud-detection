import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formatdate

##############################################################################################
### ------------------------------------ CONFIG SMTP  ------------------------------------ ### 
##############################################################################################  

smtp_server = "smtp.gmail.com" 
port = 587  

sender_email = "bankdaddys@gmail.com"  
receiver_email = ["quentin2908@gmail.com", "marcogzapro@gmail.com"]
password = "fmuieqauszmbeoix" 

############################################################################################
### ------------------------------------ EMAIL BODY ------------------------------------ ### 
############################################################################################  

msg = MIMEMultipart()
msg["Subject"] = "Alerte d'insécurité"
msg["From"] = sender_email
msg['To'] = ", ".join(receiver_email)

## Plain text
text = ""

body_text = MIMEText(text, 'plain')  
msg.attach(body_text) 

html = """
<html>
  <body>
    <p style="color:black;"> Bonjour Madame, Monsieur, </p>
    <p style="color:black;">
    Ce message vous informe qu'une fraude à été détectée sur votre compte bancaire à la Bank of Daddys. <br>
    Notre équipe y travaille déjà, si vous souhaitez plus d'informations, n'hésitez pas à nous recontacter.
    </p>
    <p style="color:black;">
    Merci pour votre compréhension, <br>
    Bien cordialement, le Departement de Protection des Clients.
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

############################################################################################
### ------------------------------------ SEND EMAIL ------------------------------------ ### 
############################################################################################  

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