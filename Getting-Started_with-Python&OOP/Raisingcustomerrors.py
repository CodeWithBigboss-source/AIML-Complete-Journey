a=int(input("enter a number between 5 and 9:"))
if(a<5 or a>9):
    raise ValueError("Enter between 5 and 9")
else:
    print("all okay")

print("everything is working")

b=input("enter string:")
if(b=="quit"):
    print("All okay again sir.")
else:
    raise ValueError("invalid input")
print("working perfectly")


# search python error classes on google to see different kinds of error which you can raise