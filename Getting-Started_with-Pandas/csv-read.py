import pandas as pd
# read_csvvv = pd.read_csv("C:\\Users\\hp\\OneDrive\\Desktop\\cricket-analysis\\matches.csv", nrows=5 ,usecols=[0])
# print(read_csvvv)
# read_csvvv = pd.read_csv("C:\\Users\\hp\\OneDrive\\Desktop\\cricket-analysis\\matches.csv", nrows=5 ,usecols=["season"])
# header changes the heading of the csv file to the value provided in header parameter and it will be used as column name
# names is used to change the column name of the csv file and it will be used as column name
# dtype is used to change the datatype of the column and it will be used as column name
# read_csvvv.head() gives first 5 rows of the csv file
# read_csvvv.tail() # gives last 5 rows of the csv file
# read_csvvv[:6] # slicing
# print(read_csvvv.to_numpy())
# read_csvvv.loc[0, "season"] = "Runs"  i didnt run it but it changes column name   
# read_csvvv.loc is used to locate data using index

read_csvvv = pd.read_csv("C:\\Users\\hp\\OneDrive\\Desktop\\cricket-analysis\\matches.csv", nrows=5 )
print(read_csvvv)
print(read_csvvv.loc[0:2])

print(read_csvvv.iloc[0:2])