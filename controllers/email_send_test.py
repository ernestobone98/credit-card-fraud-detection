import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#############Setting up the SMTP configuration

smtp_server = "smtp.gmail.com" # for Gmail
port = 587  # For starttls

sender_email = "quentinpro2908@gmail.com"  # email address used to generate password ---bankdaddys@gmail.com
receiver_email = "quentin2908@gmail.com" # a list of recipients ,"benjamin.bernaud@etu.univ-cotedazur.fr","marco.gazzera@etu.univ-cotedazur.fr","quentin.scordo@etu.univ-cotedazur.fr","ernesto.bone-bravo@etu.univ-cotedazur.fr"
password = "kjobsmahtlmgpsjh" # the 16 code generated

# if you store credentials as env variables 
# password = os.environ['EMAIL_CRED']



#############Constructing the Email

msg = MIMEMultipart()
msg["Subject"] = "Alerte Fraude"
msg["From"] = sender_email
msg['To'] = ", ".join(receiver_email)

## Plain text
text = """\
Bonjour Madame, Monsieur"""

body_text = MIMEText(text, 'plain')  
msg.attach(body_text)  # attaching the text body into msg


## HTML 
html = """\
<html>
  <body>
    <br>
    <p>
    Ce message vous informe q'une fraude à été détecter sur votre compte bancaire à la Daddys Bank. <br>
    Notre équipe est déjà sur le coup, si vous souhaiter plus d'information, n'hésiter pas à nous contacter <br><br>
    </p>
    <p>Merci de votre compréhension.</p>
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