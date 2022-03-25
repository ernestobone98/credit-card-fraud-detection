import pandas  as pd
import matplotlib.pyplot as plt
import numpy as np
from imblearn.over_sampling import SMOTE
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import make_classification
from collections import Counter
import os
import time

sep = os.path.sep
current_dir = os.getcwd()
data = pd.read_csv("models"+sep+"creditcard.csv")

# showing original data
X, y = make_classification(n_classes=2, class_sep=0.5,
    weights=[0.05, 0.95], n_informative=2, n_redundant=0, flip_y=0,
    n_features=2, n_clusters_per_class=1, n_samples=1000, random_state=10)

counter = Counter(y)

plt.subplot(121)
for label, _ in counter.items():
	row_ix = np.where(y == label)[0]
	plt.scatter(X[row_ix, 0], X[row_ix, 1], label=str(label))


# Over-sampling data with SMOTE
over_sample = SMOTE()
X_s, y_s = over_sample.fit_resample(X,y)

counter_s = Counter(y_s)


plt.subplot(122)
for label_s, _ in counter_s.items():
	row_ix_s = np.where(y_s == label_s)[0]
	plt.scatter(X_s[row_ix_s, 0], X_s[row_ix_s, 1], label=str(label_s))

plt.show()
plt.savefig(f"{current_dir}{sep}views{sep}figs{sep}fig_0", dpi=300, bbox_inches='tight', pad_inches=0)
