import matplotlib.pyplot as plt
import numpy as np
x = np.array([1,2,3,4,5])
figure,axes = plt.subplots(2,2) #two rows two columns
# targeting graph 1
axes[0,0].plot(x,x**2)
axes[0,0].set_title("X*2")
# targeting graph 2
axes[0,1].plot(x,x**3)
axes[0,1].set_title("X*3")
# targeting graph 3
axes[1,0].plot(x,x**4)
axes[1,0].set_title("X*4")
# targeting graph 4
axes[1,1].plot(x,x**5)
axes[1,1].set_title("X*5")
# till here graph is overlapping so we use
plt.tight_layout() # this will adjust the graph and make it look good   


plt.show()