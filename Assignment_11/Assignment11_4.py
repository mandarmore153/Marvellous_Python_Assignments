"""
Power Function Using Recursion
write a recursive function to calculate x^n.
power(2, 3)
"""


result = 1
def Power(no, power):
    global result
    if power > 0:
        result = result * no
        power -= 1
        Power(no, power)
    return result


def main():
    no = int(input("Enter a number: "))
    power = int(input("Enter the power: "))

    # Using for loop
    # result = 1
    # for i in range(1, power + 1):
    #     result = result * no
    # print(result)

    # Using recursion
    result = Power(no, power)
    print(result)

if __name__ == "__main__":
    main()        