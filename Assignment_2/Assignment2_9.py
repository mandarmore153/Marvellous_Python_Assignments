def Digit(no):    
    return len(str(no))

def main():
    
    no = int(input("Enter the Number : "))    
    
    result = Digit(no)
    print("Number of digit is :", result)
        
if __name__ == "__main__":
    main()