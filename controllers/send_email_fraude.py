import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formatdate

#############Setting up the SMTP configuration

smtp_server = "smtp.gmail.com" # for Gmail
port = 587  # For starttls

sender_email = "bankdaddys@gmail.com"  # email address used to generate password ---bankdaddys@gmail.com 
receiver_email = ["quentin2908@gmail.com", "marcogzapro@gmail.com"] # a list of recipients ,"benjamin.bernaud@etu.univ-cotedazur.fr","marco.gazzera@etu.univ-cotedazur.fr","quentin.scordo@etu.univ-cotedazur.fr","ernesto.bone-bravo@etu.univ-cotedazur.fr"  ,"marcogzapro@gmail.com" , "chavy98@gmail.com"
password = "fmuieqauszmbeoix" # the 16 code generated   ---fmuieqauszmbeoix 

# if you store credentials as env variables 
# password = os.environ['EMAIL_CRED']



#############Constructing the Email

msg = MIMEMultipart()
msg["Subject"] = "Alerte Fraude"
msg["From"] = sender_email
msg['To'] = ", ".join(receiver_email)
#date = formatdate(localtime=True)

## Plain text
text = """"""

body_text = MIMEText(text, 'plain')  
msg.attach(body_text)  # attaching the text body into msg


## HTML 
html = """\
<html>
  <body>
    <p style="color:black;"> Bonjour Madame, Monsieur, </p>
    <p style="color:black;">
    Ce message vous informe qu'une fraude à été détectée sur votre compte bancaire à la Bank of Daddys. <br>
    Notre équipe y travaille déjà, si vous souhaiter plus d'information, n'hésitez pas à nous recontacter.
    </p>
    <p style="color:black;">
    Merci pour votre compréhension, <br>
    Bien cordialement, le Departement de Protection des Clients.
    </p>
    <p style="color:black;",>
    <i><strong>28, Avenue Valrose <br>
    06108 Nice Cedex 2 <br>
    tel: 04 89 15 00 00</i></strong>
    </p>
  </body>
</html>
"""

body_html = MIMEText(html, 'html')
msg.attach(body_html)  # attaching to msg



############Sending the Email



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