"""
Write a program which accept number from user and check whether that 
number is positive or negative or zero.

Input: 11   output: Positive Number
Input: -8   output: Negative Number
Input: 0   output: zero
    
"""


def Check(no):
    if no>1:
        print("Positive Number")
    elif no == 0:
        print("Zero")
    else:
        print("Negative Number") 

def main():
    print("Enter a number :")
    no = int(input())
    Check(no)


if __name__ == "__main__":
    main() 