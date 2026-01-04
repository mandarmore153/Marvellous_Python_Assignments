"""
Factorial Using Recursion
Write a recursive function to calculate factorial of a number.

"""

fact = 1
def Factorial(no):
    global fact
    
    if no >= 1:
        fact = fact * no
        no = no - 1
        Factorial(no)

    return fact  

def main():

    n = int(input("Enter a number: "))
    # using for loop
    # fact = 1
    # for i in range(1, n+1):
    #     fact = fact * i
    # print(f"The factorial of {n} is: {fact}")

    # Using recursion
    result = Factorial(n)
    print(result)
   
   

if __name__ == "__main__":
    main()