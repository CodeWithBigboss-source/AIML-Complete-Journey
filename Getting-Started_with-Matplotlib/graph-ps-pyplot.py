import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
df = pd.read_csv("data.csv")
type_count= df["Type1"].value_counts(ascending=True)#value counts will give us the count of each type of item in the type1 column
plt.barh(type_count.index,type_count.values)
plt.show()