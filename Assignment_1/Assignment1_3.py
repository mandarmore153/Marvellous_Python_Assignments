"""
Write a program which contains one function named as Add()
which accepts two numbers from user and return addition of two numbers.
input : 11 5       Output: 16
   
"""

def Add(no1,no2):
    return no1+no2
    
def main():
    
    print("Enter First number :")
    no1 = int(input())
        
    print("Enter Second number :")
    no2 = int(input())

    result = Add(no1,no2)
    print("Addition is :", result)

if __name__ == "__main__":
    main()  