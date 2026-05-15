from sklearn.datasets import make_blobs
# import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
X,y =make_blobs(n_samples=5000, centers = 6, n_features = 5)
plt.scatter(X[:,0],X[:,1],c=y)
plt.show()