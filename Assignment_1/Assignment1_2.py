"""
Write a program which contains one function named as ChkNum() which accept one 
parameter as number. If number is even then it should display "Even Number"
otherwise display "old Number" on console.

Input: 11       Output: Odd Number
Input : 8       Output: Even Number

"""

def ChkNum(number):
    if (number % 2) == 0:
        print("Even Number")
    else:
        print("odd Number")    


def main():
    
    print("Enter the number :")
    no = int(input())
        
    ChkNum(no)    
    
    
if __name__ == "__main__":
    main()        