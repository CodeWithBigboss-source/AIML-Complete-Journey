# Problem 1: Clean a list (VERY IMPORTANT)

# You are given:

# data = [10, "", 20, None, 30, "", 40]
# data = [10, "", 20, None, 30, "", 40]
# cleaned = [item for item in data if item!="" and item is not None]
# print("before cleaning:",data)
# print("after cleaning:",cleaned)

# print("another way of solving this problem")
# data = [10, "", 20, None, 30, "", 40]

# def is_valid(item):
#     return item != "" and item is not None

# cleaned = list(filter(is_valid, data))
# print(f"Cleaned: {cleaned}")  # [10, 20, 30, 40]

# solving using lambda fn
# data = [10, "", 20, None, 30, "", 40]

# cleaned = list(filter(lambda x: x != "" and x is not None, data))
# print(f"Cleaned: {cleaned}")  # [10, 20, 30, 40]# This is file 1
