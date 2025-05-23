"""
Area and Perimeter of Rectangle
Accept the length and width of a rectangle. 
Calculate and display the area and perimeter.

"""


# def CalArea(l,w):
#     result = l * w
#     return result

# def CalPerimeter(l,w):
#     result = 2 * (l + w)
#     return result

def main():
    l = int(input("Enter Length : "))
    w = int(input("Enter width : "))
    
    # Area = CalArea(l,w)
    # Perimeter = CalPerimeter(l,w)
    
    # print("Area : ", Area)
    # print("Perimeter : ", Perimeter)
    
    Area = lambda l, w: l * w
    Perimeter = lambda l, w: 2 * (l + w)
    
    print("Area : ", Area(l, w))
    print("Perimeter : ", Perimeter(l, w))
    
    
        
         
        
if __name__ == "__main__":
    main() 