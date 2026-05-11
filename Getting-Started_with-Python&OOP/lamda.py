# def plus(x,y):
#     return x*y

# print(plus(5,5))
# plus = lambda x , y : x + y
# print(plus(5,5))
# multiply = lambda x , y : x * y 
# print(multiply(5,5))
# # print("lambda is the sortest way to write a function")

def appl(vx,value):
    return 6 + vx(value)

cube = lambda  x : x*x*x
print(cube(5))
print(appl(cube,3))
print(appl(lambda x : x+x , 2))
