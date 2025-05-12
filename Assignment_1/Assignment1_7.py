"""
Write a program which contains one function that accept one number 
from user and returns True if number is divisible by 5 otherwise return false.

Input: 8    output: False
Input: 25   Output: True
"""

def Divisible(no):
    if (no % 5) == 0 :
        return True
    else:
        return False

def main():
    print("Enter a number :")
    no = int(input())
    result = Divisible(no)
    
    print("Result is :", result)


if __name__ == "__main__":
    main() 