def main():
    no = int(input("Enter a number: "))
    
    Square = lambda no: no ** 2
    Cube = lambda no: no ** 3
    
    print("Square :", Square(no))
    print("Cube :", Cube(no))
    
    
if __name__ == "__main__":
    main()    