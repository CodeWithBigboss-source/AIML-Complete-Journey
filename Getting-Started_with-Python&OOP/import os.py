# import os
# if (not os.path.exists("Data")):
#     os.mkdir("Data")
# for i in range(0,100):
#     os.mkdir(f"Data/Program_{i+1}")

# have used os-rename.py to rename these folders



import os

listt = os.listdir("Data")

for i in listt:
    # print(listt)
    print(os.listdir(f"Data/{i}"))