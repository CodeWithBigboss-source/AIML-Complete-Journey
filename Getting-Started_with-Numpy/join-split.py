import numpy as np

# x = np.array([1,2,3,4])
# y = np.array([5,6,7,8])
# con = np.concatenate((x,y))
# print(con)

# x = np.array([[1,2,3,4]])
# y = np.array([[5,6,7,8]])
# con = np.concatenate((x,y),axis=0)
# print(con)


# stack fn
# x = np.array([[1,2,3,4]])
# y = np.array([[5,6,7,8]])
# con = np.stack((x,y))
# con1 = np.hstack((x,y)) #row
# con2 = np.vstack((x,y))  #col
# con3 = np.dstack((x,y)) #height
# print(con)
# print()
# print(con1)
# print()
# print(con2)
# print()
# print(con3)

# split Fn
x = np.array([1,2,3,4,5,6])
# y = np.array([[5,6,7,8]])
s = np.array_split(x,3)
print(s)
# print(type(s))