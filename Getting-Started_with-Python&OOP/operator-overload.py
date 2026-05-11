class addition:
    def __init__(self, value):
        self.value = value
    def __add__(self, other):
        return self.value + other.value

a = addition(2)
b = addition(3)
print(a+b)