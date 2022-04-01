import os
from datetime import date, datetime
from fpdf import FPDF, HTMLMixin
from SMOTE import classification_report, accuracy_score, gb, y_test, y_predict
import re

sep = os.path.sep
current_dir = os.getcwd()

####################################### 
# pour l'instant cette partie est juste horrible mais j'ai pas réussi a faire autrement
def gen_html(transac_id = 0, price = 0, client_id = 0):
    date_ = date.today().strftime("%d/%m/%Y")
    time = datetime.now().strftime("%H:%M:%S")

    return f'''
    <p> Ce rapport fait état de la fraude détectée le <B>{date_}</B> a <B>{time}</B> sur la transaction n°{transac_id}.
    <p> Veuillez trouver ci-dessous les détails du résultat :
    <p>

    <ul><li><U>ID Transaction</U> : {transac_id} </li>
    <li><U>Date</U> : {date_} </li>
    <li><U>Heure</U> : {time} </li>
    <li><U>Montant de la transaction</U> : {price} EUR</li>
    <li><U>ID Client</U> : {client_id} </li></ul>\n
    <p>
 
    <p> Résultats de l'analyse :
    '''

def gen_text():
    nclass = re.sub(' +', ' ', classification_report(y_test, y_predict)).split(' ')
    res = ''
    for i in range(6):
        res += nclass[i] + ' | '
    res += 110*' '
    for j in range(6, 13):
        res+= nclass[j] + ' | '
    return res
#######################################


class PDF(FPDF, HTMLMixin):
    def __init__(self):
        super().__init__()
        self.WIDTH = 210
        self.HEIGHT = 297

    def image_logo(self):
        self.image(f'{current_dir}{sep}views{sep}img{sep}bd.jpg', x = 10, y = 10, w = 40)

    def head(self):
        self.set_font('Arial', 'B', 11)
        self.cell(self.WIDTH - 80)
        self.cell(50, 10, 'Fraud report', 0, 0, 'R')
        self.ln(20)

    def body(self, text, y=50):
        self.ln(40)
        self.set_font('Arial', 'B', 11)
        self.set_y(y)
        self.write_html(text)

    def footer(self):
        # Page numbers in the footer
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.set_text_color(128)
        self.cell(0, 10, 'Page ' + str(self.page_no()), 0, 0, 'C')

    def lines(self):
        self.set_fill_color(50, 50, 50) # outer gray rectangle
        self.rect(0, 0, self.WIDTH, self.HEIGHT, 'FD')
        self.set_fill_color(220.0, 178.0, 83.0) # 2nd outer gold rectangle
        self.rect(5.0, 5.0, 200.0,287.0,'DF')
        self.set_fill_color(255, 255, 255) # white inner rectangle
        self.rect(8.0, 8.0, 194.0,282.0,'FD')


PLOT_DIR = f'{current_dir}{sep}views{sep}reports'
filename = datetime.now().strftime("%d_%m_%Y_%H_%M")

if __name__ == '__main__':
    file = f'{current_dir}{sep}views{sep}figs{sep}fig_0.png'
    pdf = PDF()
    pdf.add_page()
    pdf.lines()
    pdf.image_logo()
    pdf.head()
    #pdf.body(gen_html())
    #pdf.body(gen_text(), y=150)
    pdf.output(f'{PLOT_DIR}{sep}Report_{filename}.pdf', 'F')
