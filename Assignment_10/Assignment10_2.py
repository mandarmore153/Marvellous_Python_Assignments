"""
Write a program which contains one lambda function which accepts two paramters
and return its multiplication.
"""

def main():

    no1 = int(input('Enter first number: '))
    no2 = int(input('Enter second number: '))

    Multiplication = lambda no1, no2 : no1 * no2
    result = Multiplication(no1,no2)
    
    print("The multiplication of", no1, "and", no2 , "is", result)

if __name__ == "__main__":
    main()