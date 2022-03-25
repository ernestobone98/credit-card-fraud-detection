from tkinter import *
from tkinter.filedialog import *
from tkinter.scrolledtext import ScrolledText
from fpdf import FPDF


def export():
    pdf = FPDF()
    pdf.add_page()
    #pdf.image(f'{current_dir}{sep}views{sep}img{sep}bd.jpg', x = 10, y = 10, w = 40)
    pdf.set_font("Arial", "", 16)
    pdf.cell(40, 10, textbox.get("1.0", END).strip())
    pdf.output(asksaveasfilename(filetypes=[("PDF file", "*.pdf")]), "F")

win = Tk()
win.title("Ecrire dans rapport")
textbox = ScrolledText(win)
textbox.pack(fill=BOTH, expand=YES)
Button(win, text="Export to PDF", command=export).pack(fill=X)
win.mainloop()