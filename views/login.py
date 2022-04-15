# -------------------------------------- Interface:  -> Fait par Marco et Ernesto  -------------------------------------- #

from subprocess import call
from tkinter import ttk, Tk
from tkinter import *
from tkinter import messagebox
import os

sep = os.path.sep
current_dir = os.getcwd()

import string
from random import *

# ------------- Génerer les caractères autorisé pour le mot de passe ------------- #
struct = string.ascii_letters + string.punctuation + string.digits 
# ------------- Génerer le mot de passe: -> Fait par Marco ------------- #

password_p = "".join(choice(struct) for x in range(randint(8,16)))
password_e1 = "".join(choice(struct) for x in range(randint(8,16)))
password_e2 = "".join(choice(struct) for x in range(randint(8,16)))

# -- Affichage -- #
print("gm801217: {}".format(password_e1))
print("be816425: {}".format(password_e2))
print("bb809906: {}".format(password_p))

# ------------- Hache les mots de passe et les stocks dans un fichier text ------------- #
password_e1_h = str(hash(password_e1))
password_e2_h = str(hash(password_e2))
password_p_h = str(hash(password_p))

with open("109111116321001013211297115115101.txt", "w") as txtfile:    
    print(": {}".format(password_e1_h), file=txtfile)
    print(": {}".format(password_e2_h), file=txtfile)
    print(": {}".format(password_p_h), file=txtfile)


def login():
    expert1 = "gm801217" 
    expert2 = "be816425" 
    patron  = "bb809906" 
    user_name = entry0.get()
    password = entry1.get()
    if (user_name == "" and password == ""):
        messagebox.showerror("", "Vous devez entrer des caractères")
        entry0.delete("0", "end")
    elif (user_name == expert1 and password == password_e1) or (user_name == expert2 and password == password_e2) or (user_name == patron and password == password_p) :
        messagebox.showinfo("", "Connexion en cours")
        entry0.delete("0", "end")
        entry1.delete("0", "end")
        window.destroy()
        if ((user_name == expert1 and password == password_e1) or (user_name == expert2 and password == password_e2)):
            call(["python3", f"views{sep}accueil_e.py", user_name])
        elif (user_name == patron and password == password_p):
            call(["python3", f"views{sep}accueil_p.py"])        
    else:
        messagebox.showwarning("", "Erreur de connexion")
        entry1.delete("0", "end")
        entry0.delete("0", "end")

def center(win):
    """
    centers a tkinter window
    :param win: the main window or Toplevel window to center
    """
    win.update_idletasks()
    width = win.winfo_width()
    frm_width = win.winfo_rootx() - win.winfo_x()
    win_width = width + 2 * frm_width
    height = win.winfo_height()
    titlebar_height = win.winfo_rooty() - win.winfo_y()
    win_height = height + titlebar_height + frm_width
    x = win.winfo_screenwidth() // 2 - win_width // 2
    y = win.winfo_screenheight() // 2 - win_height // 2
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    win.deiconify()

def main_window():
    global entry0, entry1, window
    progress_bar.stop()
    splash.destroy()
    window = Tk()
    window.geometry("520x550")
    window.title("CONNEXION BANK OF DADDYS")
    #window.iconbitmap(f'{current_dir}{sep}views{sep}img{sep}bd.ico')
    window.configure(bg = "#ffffff")
    canvas = Canvas(
        window,
        bg = "#ffffff",
        height = 550,
        width = 520,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas.place(x = 0, y = 0)

    background_img = PhotoImage(file = f"views{sep}img{sep}background_login.png")
    background = canvas.create_image(
        260.0, 275.0,
        image=background_img)

    entry0_img = PhotoImage(file = f"views{sep}img{sep}img_textBox0.png")
    entry0_bg = canvas.create_image(
        260.0, 306.5,
        image = entry0_img)

    entry0 = Entry(
        bd = 0,
        bg = "#f5f5f5",
        highlightthickness = 0)

    entry0.place(
        x = 168.5, y = 289,
        width = 183.0,
        height = 33)

    entry1_img = PhotoImage(file = f"views{sep}img{sep}img_textBox0.png")
    entry1_bg = canvas.create_image(
        260.0, 389.0,
        image = entry1_img)

    entry1 = Entry(
        bd = 0,
        bg = "#f5f5f5",
        highlightthickness = 0,
        show="*")

    entry1.place(
        x = 169.0, y = 371,
        width = 182.0,
        height = 34)

    img0 = PhotoImage(file = f"views{sep}img{sep}img0.png")
    b0 = Button(
        image = img0,
        borderwidth = 0,
        highlightthickness = 0,
        command = login,
        relief = "flat")

    b0.place(
        x = 230, y = 454,
        width = 60,
        height = 29)


    center(window)
    window.resizable(False, False)
    window.mainloop()


splash = Tk()

splash.geometry("350x210")
splash.configure(bg = "#ffffff")
splash.title("EN COURS DE CONNEXION ")
#splash.iconbitmap(f'{current_dir}{sep}views{sep}img{sep}bd.ico')
canvas = Canvas(
    splash,
    bg = "#ffffff",
    height = 210,
    width = 350,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"views{sep}img{sep}background_splash.png")
background = canvas.create_image(
    175.0, 92.0,
    image=background_img)


s = ttk.Style()
s.theme_use('clam')
s.configure('blue.Horizontal.TProgressbar',
        troughcolor  = '#d4b356',
        troughrelief = 'flat',
        background   = 'white')

progress_bar = ttk.Progressbar(splash, orient=HORIZONTAL, length=150, mode='determinate')
progress_bar.pack(pady=10)
progress_bar.start(10)

splash.resizable(False, False)
center(splash)
splash.after(3200, main_window)    
splash.mainloop()