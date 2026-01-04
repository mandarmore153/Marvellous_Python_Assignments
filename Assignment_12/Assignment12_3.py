class Arthmatic:
    
    def __init__(self):
        self.Value1 = 0
        self.Value2 = 0

    def Accept(self):
        self.Value1 = int(input("Enter first value: "))
        self.Value2 = int(input("Enter second value: "))

    def Addition(self):
        return self.Value1 + self.Value2

    def Subtraction(self):
        return self.Value1 - self.Value2

    def Multiplication(self):
        return self.Value1 * self.Value2

    def Division(self):
        if self.Value2 == 0:
            return "Division by zero is not allowed."
        return self.Value1 / self.Value2


Obj1 = Arthmatic()
Obj1.Accept()

print("Addition: ", Obj1.Addition())
print("Subtraction: ", Obj1.Subtraction())
print("Multiplication: ",  Obj1.Multiplication())
print("Division: ", Obj1.Division())

Obj2 = Arthmatic()
Obj2.Accept()
print("Addition: ", Obj2.Addition())
print("Subtraction: ", Obj2.Subtraction())
print("Multiplication: ", Obj2.Multiplication())
print("Division: ", Obj2.Division())