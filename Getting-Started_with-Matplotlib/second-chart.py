import matplotlib.pyplot as plt
import numpy as np
x = np.array([2021,2022,2023,2024,2025])
y = np.array([81,86,75,90,95])
y2 = np.array([20,30,40,50,90])
graph_colors =dict (marker='.',markersize=15,markerfacecolor='black',linestyle='dashed')


# title
plt.title("Graph",fontsize=20,fontweight='bold',color='red')
# xlabel
plt.xlabel("Years",fontsize=15,fontweight='bold',color='blue')
# ylabel
plt.ylabel("Values",fontsize=15,fontweight='bold',color='blue')
# xticks
plt.xticks(x,rotation=45,fontsize=10,color='green')
# yticks
plt.yticks(np.arange(0,101,10),fontsize=10,color='purple')
# tick parameters
plt.tick_params(axis='both',direction='inout',length=10,width=2,color='orange')
# subplots adjustment
plt.subplots_adjust(left=0.1,right=0.9,top=0.9,bottom=0.1)
plt.plot(x,y,**graph_colors)
plt.show()