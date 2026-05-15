from sklearn.datasets import load_breast_cancer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler

X, y = load_breast_cancer(return_X_y=True)

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

from sklearn.model_selection import cross_val_score
clf = KNeighborsClassifier()

scores = cross_val_score(clf, X_scaled, y, cv = 5)
print(scores)

import numpy as np
np.mean(scores)