"""
Accept a number from the user and print its multiplication table up to 10.
"""

def main():
    
    print("Enter a number : ")
    no = int(input())
    i = 1
    while i <= 10:
        print(f"{no} * {i} = {no * i}")
        i += 1


if __name__ == "__main__":
    main()