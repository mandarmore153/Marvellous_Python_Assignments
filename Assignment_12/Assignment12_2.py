"""Class name - Circle
instance variables - Radius, Area, Circumference
class variables - PI = 3.14
instance method - Accept(),CalculateArea(), CalculateCircumference(), Display()

Accept() - Accepts the radius of the circle from the user
"""

class Circle:
    PI = 3.14

    def __init__(self):
        self.Radius = 0.0
        self.Area = 0.0
        self.Circumference = 0.0

    def Accept(self):
        self.Radius = float(input("Enter the radius of the circle: "))

    def CalculateArea(self):
        self.Area = Circle.PI * (self.Radius ** 2)

    def CalculateCircumference(self):
        self.Circumference = 2 * Circle.PI * self.Radius

    def Display(self):
        print("Radius of the circle: ", self.Radius)
        print("Area of the circle: ", self.Area)
        print("Circumference of the circle: ", self.Circumference)

Obj1 = Circle()
Obj2 = Circle()

Obj1.Accept()
Obj1.CalculateArea()
Obj1.CalculateCircumference()
Obj1.Display()

Obj2.Accept()
Obj2.CalculateArea()        
Obj2.CalculateCircumference()
Obj2.Display()
