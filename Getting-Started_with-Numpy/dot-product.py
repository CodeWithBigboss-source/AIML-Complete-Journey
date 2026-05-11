import numpy as np

# dot product in array and matrixes
# x = np.array([1,2,3,4])
# y = np.array([5,6,7,8])
# print(x.dot(y))
# print(x@y) #multiplication operator also works for dot product in 1d arrays

# x = np.array([[1,2,3,4],[1,2,3,4]])
# y = np.array([[1,2],[3,4],[5,6],[7,8]])
# print(x)
# print(x.dot(y))
# print(x@y)

# transpose  and swapaxes
# x = np.matrix([[1,2,3],[4,5,6]])
# print(x)
# print(x.T)
# print(np.transpose(x))
# print(np.swapaxes(x,0,1))

# inverse
# x = np.matrix([[1,2,3],[4,5,6]])
# print(x)
# print(np.linalg.pinv(x))   #linal.inv is only working for square matrixes but pinv is working for non square matrixes also
# print(x.I)
# y = x.dot(x.I)
# print(y)

#matrix power fn
# x = np.matrix([[1,2],[3,4]])
# print(x)
# y = np.linalg.matrix_power(x,2)
# print(y)

# determinant
x = np.matrix([[1,2],[3,4]])
print(x)
print(np.linalg.det(x))