import matplotlib.pyplot as plt
import numpy as np
# Pie chart data
labels = ['Protein', 'Carbs', 'Fats', 'Vitamins', 'Minerals']
sizes = [20, 30, 40, 50, 90]
# colors
colors = ['#ff9999','#66b3ff','#99ff99',"red","orange"]
# Create a pie chart    
plt.pie(sizes, labels=labels, autopct="%1.1f%%",colors=colors, explode=(0, 0, 0, 0, 0.1))  # explode the first slice
# plt.axis('equal')  # Equal aspect ratio ensures that pie chart is circular.
# plt.title("Nutrient Distribution", fontsize=20, fontweight='bold', color='red')
plt.show()