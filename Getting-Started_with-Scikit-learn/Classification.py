from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

X,y = load_breast_cancer(return_X_y=True)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)


# from sklearn.linear_model import LogisticRegression  we can also use this as it is also a classification model 
# So if we want to use logistic regression then we just need to change the line 20 clf = (your desired model)



from sklearn.neighbors import KNeighborsClassifier
clf = KNeighborsClassifier()
clf.fit(X_train_scaled,y_train)

print(clf.score(X_test_scaled, y_test))

single_instance = X_test_scaled[1]

print(clf.predict([single_instance]))

print(y_test[1])