def factor(no, sum =0):
    for i in range(1, no):        
        if  (no % i) == 0:
            sum += i
    return sum        


def main():
    
    no = int(input("Enter the Number : "))    
    
    result = factor(no)
    
    print("Result of factor is : ", result)    
        
        
if __name__ == "__main__":
    main()