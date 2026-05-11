class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.version = 2.0

p = Person("Ahsan", 25)
print(p.__dict__)
print(p.__dir__)
print(help(Person))

x = [2,3,4,5]
print(dir(x))