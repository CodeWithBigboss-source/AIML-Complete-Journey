from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

X,_ = make_blobs(n_samples = 5000, centers = 5, random_state = 10)
print(X)

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
# print(X_scaled)

import matplotlib.pyplot as plt
plt.scatter(X_scaled[:,0], X_scaled[:,1])
plt.show()



from sklearn.datasets import make_moons
X, _ = make_moons(n_samples = 5000, noise = 0.05)

kmeans = KMeans(n_clusters = 5)
kmeans.fit(X)

plt.scatter(X[:,0],X[:,1], c = kmeans.labels_)
plt.show()

kmeans = KMeans(n_clusters = 2)
kmeans.fit(X)

plt.scatter(X[:,0],X[:,1], c = kmeans.labels_)
plt.show()