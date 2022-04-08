from tkinter import *
from tkinter import filedialog
from tkPDFViewer import tkPDFViewer as pdf
import os 

# pip install tkPDFViewer
# https://www.youtube.com/watch?v=BwFQmGysFNE&t=627s # check the difference

win = Tk()
win.geometry("630x700+400+100")
win.title("Ouvrir rapports")
win.config(bg = "white")

def browseFiles():
	filename = filedialog.askopenfilename(initialdir = os.getcwd(), 
										title = "Select a pdf file", 
										filetype = (("PDF FILE", ".pdf")))
	
	variable1 = pdf.ShowPdf()
	#Add your pdf location and width and height.
	variable2 = variable1.pdf_view(win,pdf_location=r"location",width=50,height=100)
	variable2.pack()

Button(win, text="Open", command=browseFiles, width = 40, font ="Arial 20", bd = 4).pack()

win.mainloop()
