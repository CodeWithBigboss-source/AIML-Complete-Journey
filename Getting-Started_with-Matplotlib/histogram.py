import matplotlib.pyplot as plt
import numpy as np

data = [10,20,20,30,30,30,40,40,50]

plt.hist(
    data,
    bins=5,
    color='skyblue',
    edgecolor='black'
)

plt.title("Histogram Example")
plt.xlabel("Values")
plt.ylabel("Frequency")

plt.show()