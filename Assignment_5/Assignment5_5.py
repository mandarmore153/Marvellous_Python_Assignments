"""
Even or odd Numbe rcheck
Write a program to check whether  the entered number iss even or odd.

"""


def ChkEvenOdd(no):
    if no % 2 == 0:
        print(f"{no} is an even number.")
    else:
        print(f"{no} is an odd number.")


def main():
    no = int(input("Enter a number : "))
    
    ChkEvenOdd(no)
        
        
if __name__ == "__main__":
    main()   