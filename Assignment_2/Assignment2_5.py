def PrimeNumber(no):
    
    if no <= 1:
        print("Not Prime number")
        return
    
    for i in range(2,no):        
        if (no % i) == 0:
            print("Not Prime number")
            return
            
        
    print("Prime number")
            
              

def main():
    
    no = int(input("Enter the Number : "))    
    
    PrimeNumber(no)  
                
        
if __name__ == "__main__":
    main()