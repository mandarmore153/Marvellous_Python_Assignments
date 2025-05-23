"""
Accept a number and print its factoril using a for loop.
"""

def main():
    
    no = int(input("Enter a number : "))
    
    multi = 1
    for i in range(1, no + 1):
        multi = multi * i
        
    print("Factorial of 5 is :", multi) 


if __name__ == "__main__":
    main()