from sklearn.metrics import accuracy_score, classification_report
from joblib import load
import pandas as pd


data = pd.read_csv('models\\creditcard.csv', sep= ',')
data = data.drop(['Time', 'Amount'], axis=1)
X = data.iloc[:, data.columns != 'Class']
y = data.iloc[:, data.columns == 'Class']
mlpc = load("controllers\\MLPC.joblib")

y_predict = mlpc.predict(X)
print(accuracy_score(y, y_predict))
print(classification_report(y, y_predict))