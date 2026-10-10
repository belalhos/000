

class Student:
    name = ""
    roll = ""
    gpa  = ""

s1 = Student()

s1.name = "rahi"
s1.roll = 101
s1.gpa = 4.50

print(s1.name)


class Car:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price


my_car = Car("Toyota", 2500000)

print("Brand:", my_car.brand)
print("Price:", my_car.price)

class student:
    name = ""
    roll = ""
    gpa = ""

    def setValue(self,n,r,g):
        self.name = n
        self.roll = r
        self.gpa = g

    def showValue(self):
        print(f"Name:{self.name},Roll:{self.roll},Gpa:{self.gpa}")

tahim = student() 
tahim.setvalue("Tahim",101,4.88)
tahim.showValue()


