class animal:
    def sound(self):
        return "animal makes sound"

class cat(animal):
    def sound(self):
        return "cat says meow"

class dog(animal):
    def sound(self):
        print(super().sound())
        return "dog barks"
        

a = animal()
c = cat()
d = dog()
print(a.sound())
print(c.sound())
print(d.sound())