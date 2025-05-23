"""
Print Triangle Pattern using Nested Loop.
"""

def main():
    no = int(input("Enter a number : "))
    
    for i in range(1, no + 1):
        for j in range(1, i):
            print(" * ", end ="")
        
        print()               
        

if __name__ == "__main__":
    main()    