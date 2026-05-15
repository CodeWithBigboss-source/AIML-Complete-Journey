from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
X, y = load_iris(return_X_y=True) #loading datasets and storing in objects
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2) #model training
scaler = StandardScaler() #preprocessing using standardscaler
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
X_train_scaled #use print in vs code
import numpy as np
(X_train - np.mean(X_train, axis = 0)) / np.std(X_train,axis = 0) #this is what standardscaler is doing which we just did manually
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
X_train # this is what minmaxscaler is doing and use print fn in vs code for this line 
X_min = np.min(X_train, axis=0)
X_max = np.max(X_train, axis = 0)
(X_train - X_min) / (X_max - X_min)  #and here we did it manually what the minmaxscaler is doing exactly
print("hello")