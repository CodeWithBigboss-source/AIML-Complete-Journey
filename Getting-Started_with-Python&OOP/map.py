# def square(x):
#     return x*x
# listt=[2,3,4,5,6]
# print(square(2))
# vsquare=map(square , listt)
# print(list(vsquare))

# splus=map(lambda x : x + x , listt)
# print(list(splus))

# Filter
# def filter_function(x):
#     return x>4
# filtered_words = list(filter(filter_function,listt))
# print(list(filtered_words))
# print(filtered_words)

# Reduce
from functools import reduce
l=[1,2,3,4,5,6]
sum=reduce(lambda x,y:x+y , l)
print(sum)