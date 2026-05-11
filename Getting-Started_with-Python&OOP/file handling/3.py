# This is file 3
# Problem 5: Remove strings that are just whitespace
data = ["hello", "", "   ", "world", "  ", "python", " "]
# Expected: ["hello", "world", "python"]
cleaned = [ item for item in data if item.strip() != "" ]
print(cleaned)