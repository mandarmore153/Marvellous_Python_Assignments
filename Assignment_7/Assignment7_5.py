"""
Write a function that accetps a string and checks whether it is a palindrome.
"""
def ChkPalindrome(string):
    if string == string[::-1]:
        print(f"{string} is a palindrome")
        
    else:
        print(f"{string} is not a palindrome")    

def main():
    string = input("Enter a string: ")
    
    ChkPalindrome(string)
    

if __name__ == "__main__":
    main()
       