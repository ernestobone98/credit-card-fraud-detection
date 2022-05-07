import os
from tkinter import *
from subprocess import call
import sys
from tkinter import messagebox
from pandastable import Table
from datetime import datetime
from controllers.send_mail import get_vict, main as mail
from controllers.ml_test import n 
import threading

sep = os.path.sep

def showMessage(message, type='info', timeout=2500): #function that shows a message during a certain time
    root = Tk()
    root.withdraw()
    try:
        root.after(timeout, root.destroy)
        if type == 'info':
            messagebox.showinfo('Info', message, master=root)
        elif type == 'warning':
            messagebox.showwarning('Warning', message, master=root)
        elif type == 'error':
            messagebox.showerror('Error', message, master=root)
    except:
        pass

def generating_report():
    showMessage("I'm building the report, please wait few seconds !", timeout=5000)
t = threading.Thread(target=generating_report, name='Message when generating report')

def create_message():
    call(["python3", f"controllers{sep}write.py"])

def send_mail(model):
    victimes = get_vict(model)
    mail(victimes)
    return victimes

def msg_patron():
    exp = check_args(sys.argv)
    msg = f'''Message from the expert {exp} : 
I performed an ML analysis today at {datetime.now().strftime("%H:%M:%S")} and an email has been sent to our affected clients!
You can check the generated report as a pdf for more information.
Thanks,
Have a good day!
'''
    with open(f"views{sep}reports{sep}message_patron.txt", 'w') as f:
        f.write(msg)

def tmp_report(victimes):
    ID, surname, name, mail, tel, amount = victimes
    with open(f"_report_tmp.txt", 'w') as f:
        f.write("\\large \\textbf{\\underline{Liste des victimes}} : \\bigbreak \\normalsize ")
        
        for i in range(1, len(ID)+1):
            f.write('\\textbf{\\emph{Victime '+ str(i) + '}'+'}'+' : \\newline ')
            f.write(f"ID : {ID[i]} \\newline Prénom : {surname[i]} \\newline Nom : {name[i]} \\newline Adresse Mail : {mail[i]} \\newline Num. de Téléphone : 0{tel[i]} \\newline Montant de la fraude : {amount[i]}e \\bigbreak")

def clean_tmp():
    call(['rm', '_report_tmp.txt'])

def create_report():
    v = choice.get()
    if v != -1 : t.start() #fix the waiting message when we dont generate report
    if v == 1:
        victimes = send_mail('MLPC')
        tmp_report(victimes)
        call(['rm', f'views{sep}reports{sep}rapport_MLPC.pdf'])
        call(['pdflatex', f'controllers{sep}rapport_MLPC.tex'])
        call(['mv', 'rapport_MLPC.pdf', f'views{sep}reports{sep}rapport_MLPC.pdf'])
        call(['rm','rapport_MLPC.aux', 'rapport_MLPC.log'])
    elif v == 2:
        victimes = send_mail('RFC')
        tmp_report(victimes)
        call(['rm', f'views{sep}reports{sep}rapport_RFC.pdf'])
        call(['pdflatex', f'controllers{sep}rapport_RFC.tex'])
        call(['mv', 'rapport_RFC.pdf', f'views{sep}reports{sep}rapport_RFC.pdf'])
        call(['rm','rapport_RFC.aux', 'rapport_RFC.log'])
    elif v == -1:
        messagebox.showerror("Error", "You must select a model before generating the report !")
        return 1
    messagebox.showinfo("Done", "The report has been generated successfully !")
    msg_patron()
    clean_tmp()
    t.join()

def log_out():
    window.destroy()
    call(['clear'])
    call(["python3", f"views{sep}login.py"])

def check_args(args):
    if len(args) != 2:
        print("Error ! \t Usage : python3 -m accueil_e.py [username]")
        sys.exit(1)
    else:
        if sys.argv[1] != 'be816425' and sys.argv[1] != 'gm801217':
            print("Error ! \t Unknown username")
            sys.exit(1)
    if sys.argv[1] == 'be816425' : return 2
    elif sys.argv[1] == 'gm801217': return 1

check_args(sys.argv)

# ------------- Ml_test for help the print of table ------------- #
n = n()

# -------------------------- #
window = Tk()
window.geometry("1200x720")
window.title("Expert Interface")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 720,
    width = 1200,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"views{sep}img{sep}bg_inter.png")
background = canvas.create_image(
    600.0, 360.0,
    image=background_img)

img0 = PhotoImage(file = f"views{sep}img{sep}env.png")
send_message_button = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = create_message,
    relief = "flat",
    background= '#262A33')

send_message_button.place(
    x = 131, y = 373,
    width = 45,
    height = 45)

canvas.create_text(
    159.0, 433.5,
    text = "Send message",
    fill = "#ffffff",
    font = ("RalewayRoman-Regular", int(18.0)))

img1 = PhotoImage(file = f"views{sep}img{sep}logout.png")
logout_button = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = log_out,
    relief = "flat",
    background='#D8BB67')

logout_button.place(
    x = 1149, y = 25,
    width = 25,
    height = 25)

img2 = PhotoImage(file = f"views{sep}img{sep}report.png")
report_button = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = create_report,
    relief = "flat",
    background= '#262A33')

report_button.place(
    x = 131, y = 515,
    width = 45,
    height = 45)

canvas.create_text(
    161.0, 585.5,
    text = "Generate report",
    fill = "#ffffff",
    font = ("RalewayRoman-Regular", int(18.0)))

if sys.argv[1] == 'be816425':
    img3 = PhotoImage(file = f"views{sep}img{sep}ernesto.png")
    name = 'Ernesto'
elif sys.argv[1] == 'gm801217':
    img3 = PhotoImage(file = f"views{sep}img{sep}marco.png")
    name = 'Marco'

face_pic = Label(
    background='#262A33',
    image = img3,
    borderwidth = 0,
    highlightthickness = 0,
    relief = "flat")

face_pic.place(
    x = 110, y = 135,
    width = 88,
    height = 88)

canvas.create_text(
    159.0, 260.5,
    text = name,
    fill = "#ffffff",
    font = ("RalewayRoman-Regular", int(18.0)))

# ------------- Print of table ------------- #
f = Frame(bg="white",width=0,height=0)
df = n.head(10)
f.place(height=500, width=750, x=400, y=100)
pt = Table(f, dataframe=df,showtoolbar=True, showstatusbar=True)
pt.show()
 
choice = IntVar(window, -1)

# ------------- Radiobutton for reports ------------- #
Radiobutton(window, text = "MLPC", value = 1,variable = choice, background="white", indicatoron = 0, selectcolor='#d4b356').place(height=30, width=60, x=400, y=650)
Radiobutton(window, text = "RFC", value = 2,variable = choice, background="white", indicatoron = 0, selectcolor='#d4b356').place(height=30, width=60, x=475, y=650)


window.resizable(False, False)
window.mainloop()
