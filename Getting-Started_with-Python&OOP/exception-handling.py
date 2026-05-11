# a=input("enter a number: ")
# print(f"Displaying table of entered number {a}")
# try:
#     for i in range(1,11):
#         print(f"{int(a)}X{i}={int(a)*i}")
# except:    #we can also write   except Exception as e:
#     print("invalid input")

# print("see you soon")
# try:
#     b=int(input("enter an integer:"))
#     ab=[5,6]
#     print(ab[b])
# except ValueError:
#     print("Value Error enter an integer")
# except IndexError:
#     print("Index error")

print("now we will print try except and finally in a function because in interviews " \
"finally is asked that why we use finally? when we can use print also. "\
"that is when we say if we"\
"use try except in a function"\
"then we can not use print to print the statement thta is why we use finally!")

def Testing():
    try:
        l=[33,44,55,66]
        i=int(input("Enter index:"))
        print(l[i])
        return 1
    except ValueError:
        print("Enter an integer")
        return 0
    finally:
        print("Ended")

x=Testing()
print(x)

