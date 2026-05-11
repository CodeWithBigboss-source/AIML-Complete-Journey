dic={"ahsan":"pass",
     "ashir": "fail",
     "abuzar": "pass"}
# print(dic)
# print(dic["ashir"])
# print(dic.get("ashir"))
print(dic.keys())
print(dic.values())
# for keys in dic.keys():
#     print(dic[keys])
dic2={"ahmed": "pass",
      "ali":"pass",
      "daniyal":"pass",
      "umar": "fail"}
print(dic2)
dic.update(dic2)
print(f"updated dic is {dic}")
print("clearing dictionary using clear function")
dic.clear()
print(dic)