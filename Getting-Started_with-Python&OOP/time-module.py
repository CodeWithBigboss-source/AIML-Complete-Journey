import time

# def usingwhile():
#     i= 0
#     while(i<10000):
#         i=i+1
#         print(i)
# def usingfor():
#     for i in range(10000):
#         print(i)

# init = time.time()
# usingfor()
# t1 = time.time() - init
# init = time.time()
# usingwhile()
# print(time.time()-init)
# print(t1)

# time.sleep(3)
# print("this was printed after 3 seconds")
t= time.localtime()
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S",t)
print(formatted_time)