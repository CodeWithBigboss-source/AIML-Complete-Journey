import pandas as pd
# dic = {"Name":["Ahsan","ALi","Ahmed"],"Age":[20,21,22],"Job":["Student","Teacher","Engineer"]}
# y = pd.DataFrame(dic)
# y = pd.DataFrame(dic, columns=["Name","Age","Job"])
# print(y)

# how to get data using index
dic = {"Name":["Ahsan","ALi","Ahmed"],"Age":[20,21,22],"Job":["Student","Teacher","Engineer"]}
y = pd.DataFrame(dic)
print(y["Name"][2])
l = [1,2,3,4,5,6]
m = pd.DataFrame(l)
print(m)
print(m[0][0])