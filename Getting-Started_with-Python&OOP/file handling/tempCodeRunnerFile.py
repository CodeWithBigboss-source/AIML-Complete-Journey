# This is file 6
# Problem 8: Remove empty lists, tuples, and dictionaries
data = [1, [], 2, {}, 3, (), 4, [5], {"a": 1}]
# Expected: [1, 2, 3, 4, [5], {"a": 1}]
cleaned = [item for item in data if not isinstance(item,(list,dict,tuple)) or len(item)!=0]
print(cleaned)