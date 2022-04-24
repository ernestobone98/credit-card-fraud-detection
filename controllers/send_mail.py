from ml_test import main
import os
from subprocess import call

sep = os.path.sep

victimes = main()
print(victimes)

ID = list(victimes['ID'])
Surname = list(victimes[' Prenom'])
Name = list(victimes[' Nom'])
Mail = list(victimes[' Adresse mail'])

print(ID, Surname, Name, Mail)

for prenom, nom, mail, id in zip(Surname, Name, Mail, ID):
    call(['python3', f'controllers{sep}send_email_fraude.py', prenom, nom, mail, str(id)])