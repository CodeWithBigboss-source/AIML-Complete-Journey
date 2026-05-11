import numpy as np
# changes made in x(or original data) will not affect copy and vice virsa but in view changes made in original or view affect both
# x = np.array([1,2,3,4])
# co = x.copy()
# print(x)
# print(co)

x = np.array([1,2,3,4])
v = x.view()
print(x)
print(v)
