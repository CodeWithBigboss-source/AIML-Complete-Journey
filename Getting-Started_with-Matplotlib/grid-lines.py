import matplotlib.pyplot as plt
# Sample data
x = [2021,2022,2023,2024,2025]
y = [81,86,75,90,95]
# Plotting the graph
plt.plot(x,y)
# Adding grid lines
# plt.grid()
# only lines not blocks
plt.grid(axis="y",linewidth=0.5)
plt.show()