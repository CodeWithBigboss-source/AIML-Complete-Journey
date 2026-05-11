def mygen():
    for i in range(100000):
        yield i

gen = mygen()
# print(next(gen))
# print(next(gen))
# print(next(gen))
for j in gen:
    print(j)