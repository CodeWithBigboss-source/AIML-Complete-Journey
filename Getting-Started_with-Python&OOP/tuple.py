# tup=(1,2,3,4,5,6,7,"ahsan",True)
# print(type(tup),tup)
# print(tup[1])
# print(tup[-1]) #true
# print(tup[-5]) #5
# print(tup[6])
# print(len(tup))
# if 7 in tup:
#  print("it is in the tuple")
# else:
#  print("not present")

print("now we will perform operatons of tuple")
countries=("Pakistan","India","UK","USA","UAE","Turkey",)
print(countries)
temp=list(countries)
temp.append("USSR")
temp.pop(1)
temp[3]="Austria"
countries=tuple(temp)
print(countries)