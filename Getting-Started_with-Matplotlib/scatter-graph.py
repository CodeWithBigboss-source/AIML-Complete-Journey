import matplotlib.pyplot as plt
# Sample data
x = [1,2,3,4,5,6,7,9] #Hours
y = [22,33,44,55,66,77,88,99]
x1 = [1,2,3,4,5,6,7,9] #Hours
y1 = [32,43,54,56,76,87,43,98]
plt.scatter(x,y,label = "Class A")
plt.scatter(x1,y1,label = "Class B")

plt.legend()
plt.show()
