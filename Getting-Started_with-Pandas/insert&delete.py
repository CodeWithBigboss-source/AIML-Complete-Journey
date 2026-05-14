import pandas as pd
# dic = pd.DataFrame({"Name":["Ahsan","ALi","Ahmed"],"Age":[20,21,22],"Job":["Student","Teacher","Engineer"]})
# dic.insert(1,"City",["Karachi","Lahore","Islamabad"])
# print(dic)
# dic["R-age"] = dic["Age"][:2]
# print(dic)   #we performed slicing here and only 2 values are added in the new column because we sliced only 2 values from the "Age" column.

var = pd.DataFrame({"A":[1,2,3],"B":[4,5,6]})
print(var)
print()
var1 = var.pop("B")
print(var)
print()
print(var1)
print()
del var["A"] #del deletes the column permanently and we cannot access it again but pop just removes the column from the dataframe but we can access it again using the variable in which we stored the popped column.
print(var)