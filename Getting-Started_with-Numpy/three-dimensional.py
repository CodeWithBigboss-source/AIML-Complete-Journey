import numpy as np
# x = np.array([[[1,1,1,1],[2,2,2,2],[3,3,3,3]]])
# print(x)
# print(x.ndim)

# multi dimensional array
x = np.array([[[[[[[[[[1,1,1,1],[1,1,1,1],[1,1,1,1,],[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]]]]]]]]]])
print(x)
print(x.ndim)
y = np.array([1,2,3,4],ndmin=10)
print(y)