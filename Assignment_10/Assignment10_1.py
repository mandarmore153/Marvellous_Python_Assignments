"""
Write a program which contains one lambda function which accepts one paramter and return power of two.
"""

def main():
    no = int(input('Enter a number: '))
    Square = lambda no : no ** 2
    result = Square(no)
    print("The square of", no, "is", result)

if __name__ == "__main__":
    main()