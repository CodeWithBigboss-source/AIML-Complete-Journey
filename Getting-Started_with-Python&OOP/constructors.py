class office:
    def __init__(self,name,age):
        print("constructor is working")
        self.name=name 
        self.age=age
    def info(self):
        print(f"{self.name} is {self.age} years old")

a=office("ahsan",25)
b=office("nasar",55)

a.info()
b.info()
