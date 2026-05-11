# This is file 5
# Problem 7: Remove outliers (numbers > 100 or < 0)
data = [25, 150, 30, -10, 45, 200, 50, 75, -5, 100]
# Expected: [25, 30, 45, 50, 75, 100]
cleaned = [item for item in data if 0<item<100]
print(cleaned)
