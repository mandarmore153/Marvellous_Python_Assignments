"""
Print Number Using Recursion
Write a recursivefunction to print numbers from 1 to N.

"""


i = 1
def sequence(value):
    global i
    if i <=  value:
        print(i, end=' ')
        i += 1
        sequence(value)

def main():

    n = int(input("Enter a number: "))
    # using for loop
    # for i in range(1, n+1):
    #     print(i, end=' ')

    sequence(n)

if __name__ == "__main__":
    main()