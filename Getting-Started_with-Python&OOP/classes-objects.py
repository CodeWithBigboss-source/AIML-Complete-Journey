# class books:
#     name = "Forty Rules of Love"
#     Author = "Elif Shafak"
#     Price = 1500

# a = books
# print(a.name,a.Author,a.Price)

class books:
    name = "Forty Rules of Love"
    Author = "Elif Shafak"
    Price = 1500
    def info(self):
        print(f"{self.name} is written by {self.Author}")

a = books()
a.info()