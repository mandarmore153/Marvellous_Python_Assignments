def SearchElement(input_elements, serach_element, count = 0):
    for i in input_elements:        
        if serach_element == i:
            count += 1
            
    return count        


def main():
    no = int(input("Number of element : "))
    
    input_elements = []
    
    for i in range(no):
        elements = int(input())
        input_elements.append(elements)
        
    print(input_elements) 

    serach_element = int(input("Enter element to search : "))

    Result = SearchElement(input_elements, serach_element)    
            
    print("frequrncy of search number is : ", Result)        

if __name__ == "__main__":
    main()