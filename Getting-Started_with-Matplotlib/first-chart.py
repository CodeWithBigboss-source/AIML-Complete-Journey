import matplotlib.pyplot as plt
x = [2021,2022,2023,2024,2025]
y = [81,86,75,90,95]
y2 = [20,30,40,50,90]
graph_colors =dict (marker='.',markersize=15,markerfacecolor='black',linestyle='dashed')
plt.plot(x,y,**graph_colors)
# if we make a dictionary and store all the color detils in it then we can use it  at every graph
plt.plot(x,y2,**graph_colors)
plt.show()
# use color ppicker for custom colors