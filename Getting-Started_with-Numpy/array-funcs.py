import numpy as np
# x = np.array([1,2,3,4])
# print(np.min(x))
# print(np.max(x))


# video 8 of numpy
# x = np.array([[1,2,3,4],[5,6,7,8]])
# print(np.min(x,axis=0),np.argmin(x))
# print(np.max(x,axis=0),np.argmax(x))

# square root
# x = np.array([[4,6,81,64],[91,8,8,144]])
# var = np.sqrt(x)
# print(var)

# sin cos and cumsum
x = np.array([[4,6,81,64],[91,8,8,144]])
var = np.sin(x)
print(var)
var = np.cos(x)
print(var)
var = np.cumsum(x)
print(var)