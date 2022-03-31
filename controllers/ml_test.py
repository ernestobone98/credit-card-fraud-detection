from os import sep
from matplotlib.axis import Axis
import pandas  as pd
import matplotlib.pyplot as plt
import numpy as np
from imblearn.over_sampling import SMOTE
from sklearn.svm import SVC
from collections import Counter
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import StandardScaler

data = pd.read_csv('models\\creditcard.csv', sep= ',')
data = data.drop(['Time', 'Amount'], axis=1)

X = data.iloc[:, data.columns != 'Class']
y = data.iloc[:, data.columns == 'Class']
# X = data.drop(['Class'], axis=1)
# y = data['Class']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

print("valores de X")
print(X_train.sample(n=1000))
print("Valores de y")
print(y_train.sample(n=1000))

X = X.values.tolist()
y = y.values.tolist()
