"""
Accept a number from the user and check whether it it prime or not.
"""

def Chkprime(no):
    prime = True
    for i in range(2, no):
        if no % i == 0:
            prime = False
            print(f"{no} is not a prime number")
            break
        
    if prime == True:
        print(f"{no} is a prime number")    

def main():
    
    no = int(input("Enter a number : "))
    
    Chkprime(no)


if __name__ == "__main__":
    main()