"""
Count ZZeros in a Number(Recursively)
Write a rescursive function to count how much zeros are in the given number.
count_zero(1020300)
"""

count = 0
def count_zero(no):
    global count
    if no > 0:
        digit = no % 10
        if digit == 0:
            count = count + 1
        no //= 10 
        count_zero(no)
    return count        


def main():

    no = int(input("Enter a number: "))
    
    # using for loop

    # count = 0
    # while no > 0:
    #     digit = no % 10
    #     if digit == 0:
    #         count = count + 1
    #     no //= 10    

    # print(count)    

    # Using recursion
    result = count_zero(no)
    print("Number of zeros in the number is:", result)


if __name__ == "__main__":
    main()
    