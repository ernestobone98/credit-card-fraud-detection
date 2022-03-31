import pandas  as pd
import matplotlib.pyplot as plt
import numpy as np
from imblearn.over_sampling import SMOTE
from sklearn.svm import SVC
from sklearn.datasets import make_classification
from collections import Counter
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import StandardScaler

# ---------------------- preprocesing data ----------------------
data = pd.read_csv('models\\creditcard.csv', sep= ',')
# data = data.drop(['Time', 'Amount'], axis=1)

X = data.iloc[:, data.columns != 'Class']
y = data.iloc[:, data.columns == 'Class']

gb = data.groupby('Class').agg(
    transactions=('Class', 'count'),
    total_revenue=('Amount', 'sum'),
).round(2)

print(gb)
data = data.drop(['Time', 'Amount'], axis=1)

#taking just a part of data to developpe
X = X.to_numpy()[:10000]
y = y.to_numpy()
y = y.flatten()[:10000]

# ---------------------- random data generation ----------------------
# print(y.head)
# print(X.head)
# showing original data
# X, y = make_classification(n_classes=2, class_sep=0.5,
#     weights=[0.05, 0.95], n_informative=2, n_redundant=0, flip_y=0,
#     n_features=2, n_clusters_per_class=1, n_samples=1000, random_state=10)


# ---------------------- Plotting imbalance ---------------------- Problem with the graph
counter = Counter(y)

plt.subplot(121)
for label, _ in counter.items():
	row_ix = np.where(y == label)[0]
	plt.scatter(X[row_ix, 0], X[row_ix, 1], label=str(label))

# ---------------------- Splitting the data ----------------------
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)		#Dividing dataset with test_set <- 0.3*data
# sc = StandardScaler()
# X_train = sc.fit_transform(X_train)			# all data features except Class
# X_test = sc.fit_transform(X_test)			# Class feature

# ---------------------- Balancing data with SMOTE ----------------------
over_sample = SMOTE()
X_train, y_train = over_sample.fit_resample(X_train,y_train)


counter_s = Counter(y_train)
plt.subplot(122)
for label_s, _ in counter_s.items():
	row_ix_s = np.where(y_train == label_s)[0]
	plt.scatter(X_train[row_ix_s, 0], X_train[row_ix_s, 1], label=str(label_s))

plt.savefig('SMOTE.png')
plt.show()

# ---------------------- ML models ----------------------

# KNeighbors Application
model = KNeighborsClassifier()
model.fit(X_train, y_train)
y_predict = model.predict(X_test)

print(accuracy_score(y_test, y_predict))
print(classification_report(y_test, y_predict))

# SVM Application
model = SVC()
model.fit(X_train, y_train)
y_predict = model.predict(X_test)

print(accuracy_score(y_test, y_predict))
print(classification_report(y_test, y_predict))
