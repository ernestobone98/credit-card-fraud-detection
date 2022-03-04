# -------------------------------------- Interface:  -> Fait par Marco et Ernesto  -------------------------------------- #

from subprocess import call
from tkinter import ttk, Tk
from tkinter import *
from tkinter import messagebox

'''
Début du script
'''
win  = Tk()
win.title("CONNEXION BANK OF DADDYS")
win.iconbitmap('img\\logo.ico')
win.geometry("600x500")
win.resizable(False, False)
win.configure(background="black")

#Pour logo BANK OF DADDYS
img = PhotoImage(file ='img\\logo.png')
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
    user_name = txt_username.get()
    password = txt_passeword.get()
    if (user_name == "" and password == ""):
        messagebox.showerror("", "Vous devez entrer des caractères")
        txt_username.delete("0", "end")
    elif (user_name == "expert1" and password == "jesuis1") or (user_name == "expert2" and password == "jesuis2") or (user_name == "patron" and password == "jesuisp") :
        messagebox.showinfo("", "Connexion en cours")
        txt_username.delete("0", "end")
        txt_passeword.delete("0", "end")
        win.destroy()
        if (user_name == "expert1" and password == "jesuis1"):
            call(["python", "accueil_e.py"])
        elif (user_name == "expert2" and password == "jesuis2"):
            call(["python", "accueil_e.py"])
        elif (user_name == "patron" and password == "jesuisp"):
            call(["python", "accueil_p.py"])
        
    else:
        messagebox.showwarning("", "Erreur de connexion")
        txt_passeword.delete("0", "end")
        txt_username.delete("0", "end")


#Bouton pour se connecter
btn_enregistrer = Button(win, text = "Connexion", font = ("Arial", 16),bg ="#DCB253", fg = "black", command=login)
btn_enregistrer.place(x=200, y= 400, width=250)

'''
Fin du script
'''
win.mainloop()