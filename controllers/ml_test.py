import os
from sklearn.metrics import accuracy_score, classification_report
from joblib import load
import pandas as pd

sep = os.path.sep
current_dir = os.getcwd()

data = pd.read_csv(f'{current_dir}{sep}models{sep}creditcard.csv', sep= ',')
X_exp = data.iloc[:, data.columns != 'Class']
data = data.drop(['Time', 'Amount'], axis=1)
X = data.iloc[:, data.columns != 'Class']
y = data.iloc[:, data.columns == 'Class']
mlpc = load(f'{current_dir}{sep}controllers{sep}MLPC.joblib')
rfc = load(f'{current_dir}{sep}controllers{sep}RFC.joblib')

def main():
    # y_predict = mlpc.predict(X)
    # print(accuracy_score(y, y_predict))
    # print(classification_report(y, y_predict))

    # y_predict = rfc.predict(X)
    # print(accuracy_score(y, y_predict))
    # print(classification_report(y, y_predict))

    f = data['Class'] == 1
    f = data[f].head(3)

    nf = data['Class'] == 0
    nf = data[nf].head(10)

    print(f)
    print(nf)

    # n est un dataframe qui contient 10 transactions normaux et 3 frauduleusse qui vont etre utiliser comme demo dans l'interface de l'exper
    n = f.append(nf)
    n = n.iloc[:, data.columns != 'Class'].sample(13).reset_index(drop=True)
    print(n)
    print(rfc.predict(n))

if __name__ == '__main__':
    main()