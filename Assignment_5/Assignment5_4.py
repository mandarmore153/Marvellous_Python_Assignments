"""
Find Largest Among Three Numbers
Accept three numbers from the user and print the largest using
if-else statement.
"""

def main():
    
    no1 = int(input("Enter the first number: "))
    no2 = int(input("Enter the second number: "))
    no3 = int(input("Enter the third number: "))
    
    if no1 > no2 and no1 > no3:
        print("The largest number is:", no1)
        
    elif no2 > no1 and no2 > no3: 
        print("The largest number is:", no2)
    
    else: 
        print("The largest number is:", no3)   
    
    

if __name__ == "__main__":
    main()