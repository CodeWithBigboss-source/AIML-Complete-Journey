# i=int(input("enter value of i: "))
# while(i>0):
#     print("hi")
#     i=i-1

# print("now we will emulate a do while loop in python")
# while True:
#     j=int(input("enter number: "))
#     if(j==1):
#         break
# print("ended")

for i in range(10):
    print("5 x ",i+1," = ",(i+1)*5)
    if(i==8):
        break
print("i quit")