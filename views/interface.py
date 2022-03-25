# -------------------------------------- Interface:  -> Fait par Marco et Ernesto  -------------------------------------- #

from subprocess import call
from tkinter import ttk, Tk
from tkinter import *
from tkinter import messagebox

import string
from random import *
import os

sep = os.path.sep

# ------------- Génerer les caractères autorisé pour le mot de passe ------------- #
struct = string.ascii_letters + string.punctuation + string.digits 

# ------------- Génerer le mot de passe: -> Fait par Marco ------------- #

password_p = "".join(choice(struct) for x in range(randint(8,16)))
password_e1 = "".join(choice(struct) for x in range(randint(8,16)))
password_e2 = "".join(choice(struct) for x in range(randint(8,16)))

# -- Affichage -- #
print("Exepert 1: {}".format(password_e1))
print("Exepert 2: {}".format(password_e2))
print("Patron: {}".format(password_p))

# ------------- Hache les mots de passe et les stocks dans un fichier text ------------- #
password_e1_h = str(hash(password_e1))
password_e2_h = str(hash(password_e2))
password_p_h = str(hash(password_p))

with open("109111116321001013211297115115101.txt", "w") as txtfile:    
    print(": {}".format(password_e1_h), file=txtfile)
    print(": {}".format(password_e2_h), file=txtfile)
    print(": {}".format(password_p_h), file=txtfile)


'''
Début du script de l'interface
'''
win  = Tk()
win.title("CONNEXION BANK OF DADDYS")
#win.iconbitmap(file =f'views{sep}img{sep}logo.ico')
win.geometry("600x600")
win.resizable(False, False)
win.configure(background="black")


#Pour logo BANK OF DADDYS
img = PhotoImage(file =f'views{sep}img{sep}logo.png')
lbl_picture = Label (win, image=img)
lbl_picture.place(x = 45, y = 45)

#Pour utilisateur
lbl_username = Label (win, text="Identifiant :", font=("Arial", 15),bg="black", fg="#DCB253")
lbl_username.place(x = 125, y = 100,width = 150 )
txt_username = Entry(win,bd=4, font=("Arial", 13))
txt_username.place(x = 325, y = 100,width=200,height=30)

#Pour mot de passe
lbl_passeword = Label (win, text="Mot de passe :", font=("Arial", 15),bg="black", fg="#DCB253")
lbl_passeword.place(x = 125, y = 175,width = 150 )
txt_passeword = Entry(win,show="*",bd=4, font=("Arial", 13))
txt_passeword.place(x = 325,y = 175,width=200,height=30)

# -------------------------------------- Login: permet de gerer les connexion -> Fait par Marco et Ernesto  -------------------------------------- #
def login():
    expert1 = "ex163249" 
    expert2 = "ex263250" 
    patron  = "pa809711"
    user_name = txt_username.get()
    password = txt_passeword.get()
    if (user_name == "" and password == ""):
        messagebox.showerror("", "Vous devez entrer des caractères")
        txt_username.delete("0", "end")
    elif (user_name == expert1 and password == password_e1) or (user_name == expert2 and password == password_e2) or (user_name == patron and password == password_p) :
        messagebox.showinfo("", "Connexion en cours")
        txt_username.delete("0", "end")
        txt_passeword.delete("0", "end")
        win.destroy()
        if (user_name == expert1 and password == password_e1):
            call(["python", "views{sep}accueil_e.py"])
        elif (user_name == expert2 and password == password_e2):
            call(["python", "views{sep}accueil_e.py"])
        elif (user_name == patron and password == password_p):
            call(["python", "views{sep}accueil_p.py"])        
    else:
        messagebox.showwarning("", "Erreur de connexion")
        txt_passeword.delete("0", "end")
        txt_username.delete("0", "end")


#Bouton pour se connecter
btn_enregistrer = Button(win, text = "Connexion", font = ("Arial", 16),bg ="#DCB253", fg = "black", command=login)
btn_enregistrer.place(x=200, y= 400, width=250)

'''
Fin du script de l'interface
'''
win.mainloop()