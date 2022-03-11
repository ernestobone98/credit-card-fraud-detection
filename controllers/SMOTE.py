import pandas  as pd
import matplotlib.pyplot as plt
import numpy as np
from imblearn.over_sampling import SMOTE
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import make_classification
from collections import Counter

data = pd.read_csv('models\\creditcard.csv')

# Balancing data
X, y = make_classification(n_classes=2, class_sep=0.5,
    weights=[0.05, 0.95], n_informative=2, n_redundant=0, flip_y=0,
    n_features=2, n_clusters_per_class=1, n_samples=1000, random_state=10)

counter = Counter(y)

for label, _ in counter.items():
	row_ix = np.where(y == label)[0]
	plt.scatter(X[row_ix, 0], X[row_ix, 1], label=str(label))
plt.legend()
plt.show()

print(counter)
print('\n')