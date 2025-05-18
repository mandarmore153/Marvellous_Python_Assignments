from MarvellousNum import ChkPrime  

def ListPrime():
    no = int(input("Number of element : "))
    
    input_elements = []
    
    for i in range(no):
        elements = int(input())
        input_elements.append(elements)
        
    print(input_elements) 
    
    result = ChkPrime(input_elements)
    
    print("Total prime number is : ", result)
    
    
if __name__ == "__main__":
    ListPrime()