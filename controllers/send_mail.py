import os
from subprocess import call
import sys
from ml_test import main

def check_args(args):
    if len(args) != 2:
        print('Error ! Mismatched number of arguments\n\t Usage : send_mail.py [Model Name]')
        sys.exit(1)
    else:
        if sys.argv[1] != 'MLPC' and sys.argv[1] != 'RFC':
            print('Error ! Unknown Model\n\t Usage : send_mail.py [Model Name]')
            sys.exit(1)
    if sys.argv[1] == 'MLPC' : return 'MLPC'
    elif sys.argv[1] == 'RFC' : return 'RFC'

sep = os.path.sep

model = check_args(sys.argv)
victimes, amounts = main(sys.argv[1]) #call(['python3', f'controllers{sep}ml_test.py', model]).values.tolist()
print('COUCOU', victimes, '\n AMOUNT', amounts)

ID = list(victimes['ID'])
Surname = list(victimes['Prenom'])
Name = list(victimes['Nom'])
Mail = list(victimes['Adresse mail'])
tel = list(victimes['Tel'])

# print(ID, Surname, Name, Mail)
def main():
    for prenom, nom, mail, id in zip(Surname, Name, Mail, ID):
        call(['python3', f'controllers{sep}send_email_fraude.py', prenom, nom, mail, str(id)])
        print(f"Mail envoyé avec succes a {prenom} {nom} ! [{mail}]")
    return (ID, Surname, Name, Mail, tel, amounts)

main()