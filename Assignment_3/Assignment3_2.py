# def MaxNumber(input_elements): 
      
#     return max(input_elements)

def main():
    
    no = int(input("Number of element : "))
    
    input_elements = []
    
    for i in range(no):
        elements = int(input())
        input_elements.append(elements)
        
    print(input_elements)  
      
    # result = MaxNumber(input_elements)
    
    # print("Maximum number from list is : ", result)
    
    MaxNumber = lambda input_elements: max(input_elements)
    print("Maximum number from list is : ", MaxNumber(input_elements))
    
if __name__ == "__main__":
    main()