from sklearn.metrics import accuracy_score, classification_report
from joblib import load
import pandas as pd
import os

sep = os.path.sep

data = pd.read_csv('models{sep}creditcard.csv', sep= ',')
data = data.drop(['Time', 'Amount'], axis=1)
X = data.iloc[:, data.columns != 'Class']
y = data.iloc[:, data.columns == 'Class']
mlpc = load("controllers{sep}MLPC.joblib")

y_predict = mlpc.predict(X)
print(accuracy_score(y, y_predict))
print(classification_report(y, y_predict))