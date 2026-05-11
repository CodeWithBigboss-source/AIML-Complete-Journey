import re
text = "shere is my cat salva?"
result = re.findall("cat",text)
print(result)
text = "my number is 1234567890"
result = re.findall(r"\d",text)
print(result)