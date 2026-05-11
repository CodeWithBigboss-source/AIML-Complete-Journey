print("lets try conditional statements")
print("some conditional statements are: >,<,>=,<=,==,!=")
a=int(input("enter age: "))
if(a>18):
 print("18+")
else:
 print("underage")
b=int(input("enter money: "))
if(b>100):
 print("you can go out!")
elif(b<90):
 print("manage your badget first!")
elif(b<50):
 print("wait for monthly allowance!")
else:
 print("Take some loan!")

print("Program completed!")

print("Now we will create a nested if else loop!")
x=int(input("enter mothly expense: "))
if(x>3000):
 print("manage it!")
elif(x<1500):
 if(x>1000):
  print("hurray you are in the nested if else loop!")
else:
 print("you did not enter nested loop")
 