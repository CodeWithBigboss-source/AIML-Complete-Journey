import numpy as np
# 1d indexing then slicing
# in slicing  we write (start:stop:step)
# x = np.array([1,2,3,4])
# print(x.ndim)
# print(x[2])
# print(x[:3])

# 2D indexing then slicing
# x = np.array([[1,2,3,4],[5,6,7,8]])
# print(x.ndim)
# print(x[0,1:4])
# print(x[1,0:3])

# 3D indexing then slicing
x = np.array([[[1,2,3,4],[5,6,7,8],[9,10,11,12],[12,14,15,16]],[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]])
print(x.ndim)
# print(x)
print(x[1,1,1])