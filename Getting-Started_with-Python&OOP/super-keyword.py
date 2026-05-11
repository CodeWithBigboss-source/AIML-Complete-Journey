# class Parentclass:
#     def parent_method(self):
#         print("parent method print 1")

# class Childclass(Parentclass):
#     def child_method(self):
#         print("child method in childclass 2")
#         super().parent_method()

# p = Parentclass()
# p.parent_method()
# p2 = Childclass()
# p2.child_method()

class Programmer:
    def __init__(self,name,id):
        self.name = name
        self.id = id 

class Employee(Programmer):
    def __init__(self, name, id,lang):
        super().__init__(name, id)
        self.lang = lang

p = Programmer("ashir","111")
e = Employee("ahsan","222","php")
print(p.id,p.name)
print(e.id,e.name,e.lang)
