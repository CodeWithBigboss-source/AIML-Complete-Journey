import time
timestamp= int(time.strftime('%H'))
print(timestamp)
print("now we will see if our programs greets us accordingly or not.")
if(timestamp<=7):
    print("Good Morning")
elif(timestamp<=12):
    print("Good Afternoon")
elif(timestamp>=20):
    print("good night")
else:
    print("Its Midnight")