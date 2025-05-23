"""
Print Sum of Even Numbers Between 1 and 100.
Use a loop to find and print the sum of all even numbers from 1 and 100.

"""

def main():
    no = 1
    sum = 0
    while no <= 100:
        if no % 2 == 0:
            sum = sum + no
        no += 1

    print("The sum of even numbers from 1 to 100 is:", sum)

if __name__ == "__main__":
    main()