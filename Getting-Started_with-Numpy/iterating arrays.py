import numpy as np
# first for loop is for blocks,seconds is for rows third is for columns
# x = np.array([[1,2,3,4],[5,6,7,8]])
# for i in x:
#     for j in i:
#         print(j)

# 3d iteration
# x = np.array([[[1,2,3,4],[5,6,7,8],[9,10,11,12],[12,14,15,16]],[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]])
# for i in x:
#     for j in i:
#         for k in j:
#             print(k)

# a shortcut of above code is:
# x = np.array([[[1,2,3,4],[5,6,7,8],[9,10,11,12],[12,14,15,16]],[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]])
# for i in np.nditer(x):
#     print(i)

# x = np.array([[[1,2,3,4],[5,6,7,8],[9,10,11,12],[12,14,15,16]],[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]])
# for i in np.nditer(x,flags = ["buffered"],op_dtypes=["U"]):
#     print(i)

x = np.array([[[1,2,3,4],[5,6,7,8],[9,10,11,12],[12,14,15,16]],[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]])
for i in np.ndenumerate(x):
    print(i)
# ndenumerate function tell detail of like full shape of array