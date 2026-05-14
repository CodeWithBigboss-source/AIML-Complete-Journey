import pandas as pd
# x = pd.read_excel("C:\\Users\\hp\\OneDrive\\Desktop\\AI & MACHINE LEARNING\\Getting-Started_with-Pandas\\matches.xlsx")
# print(x)
# y = x.replace(to_replace= "2007/08", value = "2000/01")
# print(y)


# interpolation
x = pd.read_excel("C:\\Users\\hp\\OneDrive\\Desktop\\AI & MACHINE LEARNING\\Getting-Started_with-Pandas\\matches.xlsx")
print(x)
y = x.select_dtypes(include=['number'])
print(y)