import numpy as np
# # x = np.array([1,2,3,4])
# # print(x.shape)
# # y = np.array([[1,2,3,4],[5,6,7,8]])
# # print(y.shape)
# # z = np.array([
# #                 [[1,2,3,4],
# #                [5,6,7,8]],

# #                [[9,10,11,12],
# #                 [13,14,15,16]]
# #                 ])
# # print(z.shape)
# # x = np.array([1,2,3,4,5,6,7,8])
# # print(x)
# # print(x.shape)
# # print(x.ndim)   
# # y = x.reshape(4,2)
# # print(y)
# # print(y.shape)
# # print(y.ndim)   

# # 3d array reshaping
# x = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
# y = x.reshape(3,2,2)
# print(y)
# print(y.shape)
# print(y.ndim)   

# # converting 3d back to 1d
# one = y.reshape(-1)
# print (one)


# x = np.array([1,2,3,4])
# y = np.array([1,2,3,4],[1,2,3,4])
# y = np.array([[1,2,3,4],[1,2,3,4]])
z = np.array([[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]],[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]])
# print(x)
# print(y)
print(z.shape)
print(z.ndim)
print(z)
