import pandas as pd
dic = {"Name":["Ahsan","ALi","Ahmed"],"Age":[20,21,22],"Job":["Student","Teacher","Engineer"]}
df = pd.DataFrame(dic)
df.to_csv("data.csv") 