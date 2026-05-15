import matplotlib.pyplot as plt
from sklearn.datasets import make_moons
X, _ = make_moons(n_samples = 5000, noise = 0.05)

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

plt.scatter(X_scaled[:,0],X_scaled[:,1])

from sklearn.cluster import KMeans

kmeans = KMeans(n_clusters = 5)
kmeans.fit(X_scaled)

plt.scatter(X_scaled[:,0],X_scaled[:,1], c = kmeans.labels_)
plt.show()

kmeans = KMeans(n_clusters = 2)
kmeans.fit(X_scaled)
plt.show()

plt.scatter(X_scaled[:,0],X_scaled[:,1], c = kmeans.labels_)
plt.show()

from sklearn.cluster import DBSCAN
dbscan = DBSCAN(eps = 0.2)
dbscan.fit(X_scaled)

plt.scatter(X_scaled[:,0],X_scaled[:,1], c = dbscan.labels_)
plt.show()