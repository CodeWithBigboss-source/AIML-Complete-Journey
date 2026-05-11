# This is file 2
# Problem 4: Remove negative numbers
# data = [10, -5, 20, -15, 30, -25, 40, 0, 50]
# # Expected: [10, 20, 30, 40, 0, 50]
data = [10, -5, 20, -15, 30, -25, 40, 0, 50]
cleaned = [item for item in data if item>0]
print(cleaned)
