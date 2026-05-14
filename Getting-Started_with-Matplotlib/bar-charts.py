import matplotlib.pyplot as plt
import numpy as np
x = np.array(["Protein","Carbs","Fats","Vitamins","Minerals"])
y = np.array([2,1,4,3,5])
# this will display vertical bars
plt.bar(x,y)
# this will display horizontal bars
# plt.barh(x,y)
plt.show()