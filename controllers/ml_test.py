import os
from joblib import load
import pandas as pd
import sys 

sep = os.path.sep
current_dir = os.getcwd()

def check_args(args):
    if sys.argv[1] != 'MLPC' and sys.arv[1] != 'RFC':
        print('Error ! Unknown Model\n\t Usage : ml_test [Model Name]')
        sys.exit(1)
        
data = pd.read_csv(f'{current_dir}{sep}models{sep}creditcard.csv', sep= ',')
new_data = data.drop(['Time'], axis=1)
data = data.drop(['Time', 'Amount'], axis=1)
clients = pd.read_csv(f'{current_dir}{sep}models{sep}clients.csv', sep= ';')
X_exp = data.iloc[:, data.columns != 'Class']
X = data.iloc[:, data.columns != 'Class']
y = data.iloc[:, data.columns == 'Class']
mlpc = load(f'{current_dir}{sep}controllers{sep}MLPC.joblib')
rfc = load(f'{current_dir}{sep}controllers{sep}RFC.joblib')



def main(arg):
    check_args(arg)
    # y_predict = mlpc.predict(X)
    # print(accuracy_score(y, y_predict))
    # print(classification_report(y, y_predict))

    # y_predict = rfc.predict(X)
    # print(accuracy_score(y, y_predict))
    # print(classification_report(y, y_predict))

    f = new_data['Class'] == 1
    f = new_data[f].head(3)

    nf = new_data['Class'] == 0
    nf = new_data[nf].head(12)

    # print(f)
#     print(nf)
    # print(new_data.head())
    # for i in range(len(new_data)):
    #     n = random.randint(1,100)
    #     clients.append(n)
    # new_data['ID'] = clients
    # new_data = new_data.drop(['Time'], axis=1)
    # new_data.reset_index(drop=True)
    # print(new_data.head())
    # new_data.to_csv("models\\creditcard.csv")

    # n est un dataframe qui contient 12 transactions normales et 3 frauduleuses qui vont etre utilisées comme demo dans l'interface de l'expert
    n = f.append(nf)
    n = n.iloc[:, new_data.columns != 'Class'].sample(15).reset_index(drop=True)
    predictions_rfc = rfc.predict(n.drop(['Amount', 'ID'], axis=1))
    predictions_mlpc = mlpc.predict(n.drop(['Amount', 'ID'], axis=1)) 
    
    # print(predictions)
    # print(n)
    if arg == 'MLPC' : 
        n['Class'] = predictions_mlpc
    elif arg == 'RFC' :
        n['Class'] = predictions_rfc
    # print(n)
    amounts = n[['Class', 'Amount']]
    amounts = amounts[amounts['Class'] == 1]['Amount'].values.tolist()
    #amounts = n.iloc[frauds.values.tolist(), 'Amount']             
    #frauds = n.iloc[n['Class'] == 1, 'Amount']
    frauds = n[(n['Class'] == 1)] # selecting fraud amounts
    # print(frauds['ID'].values.tolist())
    # print(clients.head())
    victimes = clients[clients['ID'].isin(frauds['ID'].values.tolist())].reset_index(drop=True)
    # print(type(victimes))
    return (victimes, amounts)
