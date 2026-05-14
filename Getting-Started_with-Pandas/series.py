import pandas as pd
# x = [1,2,3,4,5,6]
# y = pd.Series(x)
# print(y)

# dic = {"Name":["Ahsan","ALi","Ahmed"],"Age":[20,21,22],"Job":["Student","Teacher","Engineer"]}
# y = pd.Series(dic)
# print(y)

# pandas can work with missing data also like it can add two series even if one contain 8 elements and the other contains 4 elements.

x = pd.Series([1,2,3,4,5,6])
y = pd.Series([1,2,3,4])
print(x+y)
