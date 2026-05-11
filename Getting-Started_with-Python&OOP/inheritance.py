class data:
    def __init__(self,name,id):
        self._name = name
        self._id = id
    def showdetails(self):
        print(f"id of {self._name} is {self._id}  ")
    
class employee(data):
    def display(self):
        print("python")

a = data("ahsan", 1)
b = employee("ashir", 2)
a.showdetails()
b.display()
