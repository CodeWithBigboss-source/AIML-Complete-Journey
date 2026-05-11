# def factorial(n):
#     if(n==0 or n==1):
#         return(1)
#     else:
#         return n * factorial(n-1)

# print(factorial(1000))

# def factorial(n):
#     print(f"Calling factorial({n})")

#     if n == 0 or n == 1:
#         print(f"Returning 1 from factorial({n})")  # base case
#         return 1
#     else:
#         result = n * factorial(n - 1)
#         print(f"Returning {result} from factorial({n})")
#         return result


# print("Final Answer:", factorial(5))

# print("now its time for fibonacci sequence!")
# def fibonaccis(n):
#     if(n==0 ):
#         return 0
#     else:
#         return ((n-1) +(n-2)
# print(fibonaccis(5))

print("now its time for fibonacci sequence!")
def fibonaccis(n):
    if(n==0 ):
        print("inside n==0")
        return 0
    elif(n==1):
        print("inside n==1")
        return 1
    else:
        print(f"now value of n is:{n}")
        return fibonaccis(n-1)+ fibonaccis(n-2)
print(f"print the result here: {fibonaccis(10)}")