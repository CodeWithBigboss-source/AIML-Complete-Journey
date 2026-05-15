# from sklearn.datasets import load_iris
# from sklearn.model_selection import train_test_split
# X, y = load_iris(return_X_y=True)
# train_test_split(X,y, test_size=0.2) #is used to view data  in the objects on jupyter
# # len(X)
# # 0.2*150
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)
# # len(X_train) used to see data
# # len(X_test)
# import numpy as np
# import matplotlib.pyplot as plt
# counts = np.bincount(y_train)
# positions = np.arange(3)
# plt.bar(positions,counts)
# plt.xticks(positions, data.target_names)


# from sklearn.model_selection import StratifiedShuffleSplit
# split = StratifiedShuffleSplit(n_splits = 1, test_size = 0.2)
# for train_idx,test_idx in split.split(X, y):
#     X_train, X_test = X[train_idx], X[test_idx]
#     y_train, y_test = y[train_idx], y[test_idx]

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.model_selection import StratifiedShuffleSplit

import matplotlib
matplotlib.use("TkAgg")
import numpy as np
import matplotlib.pyplot as plt

# Load dataset
data = load_iris()

X, y = load_iris(return_X_y=True)

# Normal split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2
)

# Count class labels
counts = np.bincount(y_train)

# Positions for bars
positions = np.arange(3)

# Draw graph
plt.bar(positions, counts)

# Add flower names
plt.xticks(positions, data.target_names)

# Print counts
print(counts)

# Show graph
plt.show()