def ListAddition(input_elements, total = 0): 
      
    for i in input_elements:
        total += i
    return total

def main():
    
    no = int(input("Number of element : "))
    
    input_elements = []
    
    for i in range(no):
        elements = int(input())
        input_elements.append(elements)
        
    print(input_elements)  
      
    result = ListAddition(input_elements)
    
    print("Addition of all element list is : ", result)
    
if __name__ == "__main__":
    main()