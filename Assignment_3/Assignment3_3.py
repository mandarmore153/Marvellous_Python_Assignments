# def MinNumber(input_elements): 
      
#     return min(input_elements)

def main():
    
    no = int(input("Number of element : "))
    
    input_elements = []
    
    for i in range(no):
        elements = int(input())
        input_elements.append(elements)
        
    print(input_elements)  
      
    # result = MinNumber(input_elements)
    
    # print("Maximum number from list is : ", result)
    
    MinNumber = lambda input_elements: min(input_elements)
    print("Maximum number from list is : ", MinNumber(input_elements))
    
if __name__ == "__main__":
    main()