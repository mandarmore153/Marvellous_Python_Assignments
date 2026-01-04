"""
Sum of First N Natural Numbers.
Write a rescursive function to calculate  sum from 1 to n.
sum_n(5)
"""
sum = 0
def sum_n(no):
    global sum
    if no > 0:
        sum += no
        no -= 1
        sum_n(no)

    return sum


def main():
    no = int(input("Enter a number: "))
    
    # Using for loop
    # sum = 0
    # for i in range(1, no + 1):
    #     sum += i
    # print(sum)    

    # Using recursion
    result = sum_n(no)
    print("sum of given number is: ", result)

if __name__ == "__main__":
    main()        