def Addition(no, total=0):
    for i in (no):
        total += int(i)
    return total 


def main():
    
    no = input("Enter the Number : ")
    
    result = Addition(no)

    print("Addition of digit is :", result)        
    
        
if __name__ == "__main__":
    main()