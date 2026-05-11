# Problem 2: Remove all falsy values (including 0, False, empty strings, None)
# data = [0, 15, "", 25, None, False, 35, "", 45, True, 55]
# Expected: [15, 25, 35, 45, True, 55]
# data = [0, 15, "", 25, None, False, 35, "", 45, True, 55]
# cleaned = [item for item in data if item!=0 and item!="" and item!=False and item is not None]
# print("Before cleaning:",data)
# print("After cleaning:",cleaned)

# Problem 3: Remove duplicates while keeping order
data = [10, 20, 10, 30, 20, 40, 10, 50, 30]
# Expected: [10, 20, 30, 40, 50]
# cleaned = []
# for item in data:
#     if item not in cleaned:
#         cleaned.append(item)
# print("before cleaning:",data)
# print("after cleaning:",cleaned)

# one way to do it
# result = []
# for item in data:
#     if(item not in result):
#         result.append(item)
# print(result)
