"""
Write a program which display first 10 even numbers on screen.
Output: 2 4 6 8 10 12 14 16 18 20

"""


def main():
    count = 0
    num = 2
    while count <10:
        
        print(num, end=" ")
        num += 2
        count += 1
    
if __name__ == "__main__":
    main() 