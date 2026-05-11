
# sets only store non duplicated data/
# sets={"ahsan",44,33,22,7,3.4}
# print(f"we will print {sets}")
# for value in sets:
#     print(value)
# empty_set={}
# print(type(empty_set))
# empty_sett=set()
# print(type(empty_sett))
# just search methods of sets in python
# print("now we will study methods of stes like union ,intersection, update, disjoint,difference,add,remove,discard,pop")
# set1={1,2,3,4,5}
# set2={4,5,6,7,8}
# print(set1)
# print(set2)
# print(f"union:{set1.union(set2)}")
# print(f"set1 after union:{set1}")
# set1.update(set2)
# print(f"set1 after update:{set1}")
# print("set1 after intersectcion: ",set1.intersection(set2))
# set1.intersection_update(set2)
# print(f"set1 afetr intersection update:{set1}")
set3={"Ahsan","Abuzar","Ashir","Maaz"}
set4={"Ahsan","Abuzar"}
set5={"Sania","Ayeza"}
print(set4.issuperset(set3))
print(set3.issuperset(set4))
print("pop,del,clear bhi imp hian aur pop jab karein ge to set main se random value pop hogi bcz unordered he")
item=set3.pop()
print(item)
print(set3)
