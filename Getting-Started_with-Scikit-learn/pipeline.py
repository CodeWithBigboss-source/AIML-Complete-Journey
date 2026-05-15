from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

X, y = load_breast_cancer(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

from sklearn.pipeline import Pipeline
pipe = Pipeline(
    [("scale", StandardScaler()),
    ("pca", PCA(n_components=10)),
    ("forest", RandomForestClassifier())
    ])
pipe.fit(X_train, y_train)

pipe.score(X_test, y_test)


# without using pipeline we would have to write all this :
from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# Load data
X, y = load_breast_cancer(return_X_y=True)

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, random_state=0
)

# STEP 1: Scaling
scaler = StandardScaler()

# Learn scaling from training data
scaler.fit(X_train)

# Transform data
X_train_scaled = scaler.transform(X_train)
X_test_scaled = scaler.transform(X_test)

# STEP 2: PCA
pca = PCA(n_components=10)

# Learn PCA from training data
pca.fit(X_train_scaled)

# Transform data
X_train_pca = pca.transform(X_train_scaled)
X_test_pca = pca.transform(X_test_scaled)

# STEP 3: Random Forest
forest = RandomForestClassifier()

# Train model
forest.fit(X_train_pca, y_train)

# Accuracy
score = forest.score(X_test_pca, y_test)

print(score)