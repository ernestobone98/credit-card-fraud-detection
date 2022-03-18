'''
Fait par Gazzera Marco:
Interface intérieur patron
'''

'''
Les import
'''

import tkinter
from tkinter import ttk, Tk
from tkinter import *
from tkinter import messagebox

'''
Début du script
'''

win  = Tk()
win.title("MENU EXPERT")
win.geometry("1400x800")
win.iconbitmap('views\\img\\logo.ico')
win.configure(background='#000000')

# Analyse les statistiques
def anlyse_stats():
	print("Analisé")

btn_analyse = Button(win, text = "Analyseur", font = ("Arial", 16),bg ="#DCB253", fg = "black", command=anlyse_stats)
btn_analyse.place(x=50, y= 25, width=1300, height=275)

# Afficher analyse des statistiques
def anlyse_stats():
	print("Affiche statistiques")

btn_analyse_stats = Button(win, text = "Analysé", font = ("Arial", 16),bg ="#DCB253", fg = "black", command=anlyse_stats)
btn_analyse_stats.place(x=50, y= 325, width=1300, height=275)

# Afficher analyse des statistiques
def comments():
	print("Commentaire")

btn_analyse_stats = Button(win, text = "Commentaire", font = ("Arial", 16),bg ="#DCB253", fg = "black", command=comments)
btn_analyse_stats.place(x=300, y= 650, width=1050, height=100)


#Pour ouvrir le rapport
def create_report():
	print("Rapport")

btn_open_report = Button(win, text = "Rapport", font = ("Arial", 16),bg ="#DCB253", fg = "black", command=create_report)
btn_open_report.place(x=50, y= 650, width=150)

'''
Fin du script
'''
win.mainloop()