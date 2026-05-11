# def CalculateGmean(a,b):
#     Gmean= (a*b)/(a+b)
#     print("Gmean: ",Gmean)

# def IsGreater(a,b):
#     if(a>b):
#         print("First number is Greater")
#     else:
#         print("First number is Greater")
# a=6
# b=3
# c=10
# d=30
# IsGreater(a,b)
# CalculateGmean(a,b)
# IsGreater(c,d)
# CalculateGmean(c,d)

# def Averagee(*numbers):
#     sum=0
#     for i in numbers:
#         sum=sum+i
#     print("average is: ",sum/len(numbers))

# Averagee(4,5,6,7,8)

def average(*numbers):
    sum=0
    for i in numbers:
        sum=sum+i
    # print("Average: ", sum/len(numbers))
    return sum/len(numbers)

c= average(3,4,5,6)
print(c)