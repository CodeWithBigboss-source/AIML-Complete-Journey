# class Info:
#     company = "Apple"
#     def show(self):
#         print(f"employee name is {self.name} and company name is {self.company} ")

#     @classmethod
#     def Changecompany(cls,newcompany):
#         cls.company = newcompany

# e1 = Info()
# e1.name= "Harry"
# e1.show()
# e1.Changecompany("Tesla")
# e1.show()
# print(Info.company)

# class methods as alternatives
class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    
    @classmethod
    def fromStr(cls, string):
        return cls(string.split("-")[0], string.split("-")[1])
    
e1 = Employee("harry", 12000)
print(e1.name)
print(e1.salary)

string = "John-12000"
e2 = Employee.fromStr(string)
print(e2.name)
print(e2.salary)