print("we are gonna practice match statement in c or c++ it is called switch statement.")
n=int(input("enter value of apples: "))
match n:
 case 6:
  print("more than 5 apples")
 case _ if(n>=10):
  print("more than 10 apples")
 case _ if(n>=20):
  print("more than 20 apples")
 case _:
  print("invalid ")