import os
from subprocess import call
from .ml_test import main as vict

sep = os.path.sep

def main(victimes):
    ID, Surname, Name, Mail, _, _ = victimes
    # print(ID, Surname, Name, Mail)
    for prenom, nom, mail, id in zip(Surname, Name, Mail, ID):
        call(['python3', f'controllers{sep}send_email_fraude.py', prenom, nom, mail, str(id)])
        print(f"Mail envoyé avec succes a {prenom} {nom} ! [{mail}]")
    # return (ID, Surname, Name, Mail, tel, amounts)

def get_vict(model):
    victimes, amounts = vict(model) 

    ID = list(victimes['ID'])
    Surname = list(victimes['Prenom'])
    Name = list(victimes['Nom'])
    Mail = list(victimes['Adresse mail'])
    tel = list(victimes['Tel'])

    return (ID, Surname, Name, Mail, tel, amounts)

#########################################################################################################

if __name__ == '__main__':
    main()