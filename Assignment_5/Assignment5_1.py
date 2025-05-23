"""
Arithmatic Operations on Two Numbers
Write a program to accepts two integers from the user and display their:

Sum
Difference
Product
Division
   
"""

def main():
    print("Enter first numbers:")
    no1 = int(input())
    
    print("Enter second numbers:")
    no2 = int(input())

    Sum = lambda no1, no2: no1 + no2
    print("Sum is:", Sum(no1, no2))
    
    Difference = lambda no1, no2: no1 - no2
    print("Difference is:", Difference(no1, no2))
    
    Product = lambda no1, no2: no1 * no2
    print("Product is:", Product(no1, no2))
    
    Division = lambda no1, no2: no1 / no2
    print("Division is:", Division(no1, no2))
    
if __name__ == "__main__":
    main()