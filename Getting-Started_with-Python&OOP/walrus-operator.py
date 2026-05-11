import shutil
shutil.copy("commandline-utility.py", "testinf-shutil.py")
# l = [1,2,3,4,5]
# while( n := len(l)) > 0:
#     print(l.pop())

foods = list()
while(food := input("what do you like to eat: ")) != "quit" : 
    foods.append(food)