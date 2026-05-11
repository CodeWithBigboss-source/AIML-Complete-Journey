class program:
    def __init__(self,num):
        self.num = num
        print(num)
    
    @staticmethod
    def staticfn(a,b):
        return a+b

a = program(4)


result = a.staticfn(2,2)
print(result)