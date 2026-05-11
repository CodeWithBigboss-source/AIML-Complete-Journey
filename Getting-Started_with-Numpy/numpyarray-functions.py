import numpy as np

# # x = np.array([1,2,3,4,5,6,7,8,9,10,2,3,4,2,5,2,2,6,4,3,2])
# # s = np.where(x == 2)
# # ss = np.where((x%2==0))
# # print(s)
# # print(ss)

# # searchsorted fn
# x = np.array([1,2,3,4,7,8,9])
# s = np.searchsorted(x,[5,6])
# print(s)
# x = np.insert(x,4,[5,6])
# print(x)

# # filter array

# x = np.array([1,2,3,4,5,6])

# filter_array = x > 3

# print(filter_array)


# shuffle function
# x = np.array([1,2,3,4,5,6])
# np.random.shuffle(x)
# print(x)

# unique fn
# x = np.array([1,1,2,2,3,2,3,5,4,5,3,2,7])
# y = np.unique(x,return_index=True,return_counts=True)
# print(y)

# flatten fn
# x = np.array([[1,2,3,4],[5,6,7,8]])
# y = x.flatten()
# print(y)
# print(x)

# ravel fn   ravel changes the original array but flatten does not change the original array
# x = np.array([[1,2,3,4],[5,6,7,8]])
# y = x.ravel()
# print(y)
# print(x)

# resize fn
x = np.array([[1,2,3,4],[5,6,7,8]])
x.resize((4, 2))
# print(y/)
print(x)