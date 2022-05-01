import os
from joblib import load
import pandas as pd
import sys 

sep = os.path.sep
current_dir = os.getcwd()

def check_args(args):
    if sys.argv[1] != 'MLPC' and sys.argv[1] != 'RFC':
        print(f'Error ! Unknown Model ({sys.argv[1]})\n\t Usage : ml_test [Model Name]\n\t Models = MLPC / RFC')
        sys.exit(1)
        
data = pd.read_csv(f'{current_dir}{sep}models{sep}creditcard.csv', sep= ',')
new_data = data.drop(['Time'], axis=1)
data = data.drop(['Time', 'Amount'], axis=1)
clients = pd.read_csv(f'{current_dir}{sep}models{sep}clients.csv', sep= ',')
X_exp = data.iloc[:, data.columns != 'Class']
X = data.iloc[:, data.columns != 'Class']
y = data.iloc[:, data.columns == 'Class']
mlpc = load(f'{current_dir}{sep}controllers{sep}MLPC.joblib')
rfc = load(f'{current_dir}{sep}controllers{sep}RFC.joblib')



def main(arg):
    check_args(arg)

    data = n()

    predictions_rfc = rfc.predict(data.drop(['Amount', 'ID'], axis=1))
    predictions_mlpc = mlpc.predict(data.drop(['Amount', 'ID'], axis=1)) 
    
    if arg == 'MLPC' : 
        data['Class'] = predictions_mlpc
    elif arg == 'RFC' :
        data['Class'] = predictions_rfc
    frauds = data[data['Class'] == 1] # selecting fraud
    amounts = data[['Class', 'Amount']]
    amounts = amounts[amounts['Class'] == 1]['Amount'].values.tolist()
    victimes = clients[clients['ID'].isin(frauds['ID'].values.tolist())].reset_index(drop=True)
    return (victimes, amounts)

def n():
    f = new_data['Class'] == 1
    f = new_data[f].head(3)

    nf = new_data['Class'] == 0
    nf = new_data[nf].head(12)

    #n is a dataframe that contains 10 normal and 3 fraudulent transactions that will be used as a demo in the expert's interface
    n = f.append(nf)
    n = n.iloc[:, new_data.columns != 'Class'].sample(15).reset_index(drop=True)
    return n



# victimes, amount = main('MLPC')
# print(f'VICTIMES = {victimes}\nAMOUNT = {amount}')
