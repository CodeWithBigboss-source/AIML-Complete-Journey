# This is file 4
# Problem 6: Keep only numeric values (int and float)
data = [10, "hello", 20.5, None, "world", 30, "40", 50.75]
# Expected: [10, 20.5, 30, 50.75]
cleaned = [item for item in data if isinstance(item,(int,float))]
print(cleaned)