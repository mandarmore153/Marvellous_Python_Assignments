"""
Create on module named as Arithmatic which contains 4 functions as Add() for addition,
Sub() for subtraction, Mult() for multiplication and Div() for division. All functions
accepts two parmeters as number and perform the operation.
Write on python program which call all the unctions from Arithmatic module by
accepting the parameters from user.
"""


from Arithmetic import Add, Sub, Mult, Div

def main():
    no1 = int(input("Enter first number : "))
    no2 = int(input("Enter second number : "))
    
    Addition = Add(no1,no2)
    print("Addition is :", Addition)
    
    Subtraction = Sub(no1,no2)
    print("Subtraction is :", Subtraction)
    
    Multiplication = Mult(no1,no2)
    print("Multiplication is :", Multiplication)
    
    Division = Div(no1,no2)
    print("Division is :", Division)

if __name__ == "__main__":
    main()