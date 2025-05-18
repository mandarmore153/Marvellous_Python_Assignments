def factorial(no, result=1):
    for i in range(1, no+1):          
        result *= i          
    return result


def main():
    
    no = int(input("Enter the Number : "))    
    
    result = factorial(no)
    
    print("Factorial result is :", result)      
        
        
if __name__ == "__main__":
    main()