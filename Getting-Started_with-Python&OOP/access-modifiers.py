# to access a private variable we need to do this
class Program:
    def __init__(self):
        self.__name = "Ahsan"

a = Program()
print(a._Program__name) #this is also called name mangling