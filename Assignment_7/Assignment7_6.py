"""
Write a function that accepts a list of integers and 
return alist of prime numbers using filter().
"""


def prime_number(no):
    prime = True
    for i in range(2, no):
        if no % i == 0:
            prime = False
            break
        
    if prime == True:
        return no    

def main():
    no = int(input("Enter a number: "))
    lst = []
    for i in range(no):
        lst.append(int(input()))
    print("List of numbers:", lst)
    
    Prime_numbers = list(filter(prime_number, lst))
    
    print("Prime numbers :", Prime_numbers)    

if __name__ == "__main__":
    main()