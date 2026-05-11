# marks=[33,44,55,"Ahsan",True]
# print(marks)
# print(type(marks))
# print(marks[1])
# print(marks[3])
# print("now  we will convert negative indexing into positive indexing and we will get same\n" \
# " result from all these print statements ")
# print(marks[-4])
# print(marks[len(marks)-4])
# print(marks[5-4])
# print(marks[1])

# if 33 in marks:
#     print("yes")
# else:
#     print("No")

# if "Ahsan" in marks:
#     print("yes")
# else:
#     print("no")
# lst=[i for i in range(4)]
# print(lst)

# lsst=[]
# for i in range(5):
#     lsst.append(i)

# print("Now we will work on methods of list like append or sort")
# list1=[3,2,4,6,5,1,7,44,33,11,99,555]
# print(list1)
# list1.append(1000)
# print(list1)
# list1.sort()
# print(list1)
# list1.sort(reverse=True)
# print(list1)
# list1.reverse()
# print(list1)

# lists=[1,2,3,4,5,6]
# print(lists)
# m=lists
# m[0]=0
# print(lists)

# lists=[1,2,3,4,5,6]
# print(lists)
# m=lists.copy()
# m[0]=0
# lists.insert(3,899) #insert function is used to change the value of a particular index as mentioned in the function
# print(lists)

# l.extend function aik list k agay dusri list attach krne ko kehte hain
m=[3,3,3,3,3,2,2,2]
print(m)
l=[6,5,4,3,1,1]
print(l)
l.extend(m)
print(l)
k=l+m
print(k)
