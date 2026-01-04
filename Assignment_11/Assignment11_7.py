"""
Print Pattern Using Recursion(Right Triangle)
Write a rescursive function to print the following pattern:
*
* *
* * *
* * * *

"""

def pattern(no):    
    if no > 0:
        pattern(no - 1) 
        for i in range(1, no + 1):
            print('*', end=' ')
        print()
        

def main():
    no = int(input("Enter a number: "))
    
    # Using for loop
    
    # for i in range(1, no):
    #     for j in range(1, i + 1):
    #         print('*', end=' ')
    #     print()   

    # Using recursion
    pattern(no)
    

if __name__ == "__main__":
    main()        