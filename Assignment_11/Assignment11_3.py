"""
Sum of Digits
Write a recursive function to calculate the sum of digits of a number.
"""

sum = 0
def sum_of_digits(no):
    global sum
    if no>0:
        digit = no % 10
        sum = sum + digit
        no //= 10
        sum_of_digits(no)
    return sum
    
def main():

    no = int(input("Enter a number: "))


    # using for while loop
    # sum = 0
    # while no > 0:
    #     digit = no % 10
    #     sum = sum + digit
    #     no //= 10
    # print(f"The sum of digits is: {sum}")
    
    # Using recursion   
    result = sum_of_digits(no)
    print(f"The sum of digits is: {sum}")
   

if __name__ == "__main__":
    main()