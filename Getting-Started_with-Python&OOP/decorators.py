def greet(fx):
    def mfx(*args,**kwargs):
        print("good morning")
        fx(*args,**kwargs)
        print("welcom to the decorator")
    return mfx

@greet 
def hello():
    print("hellow world")

@greet
def add(a,b):
    print(a+b)

hello()
add(2,2)
 