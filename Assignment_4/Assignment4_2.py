def main():
    
    a = int(input("Enter first number: "))  
    b = int(input("Enter seccond number: ")) 

    Multi = lambda a, b : a * b
    print("Multiplication is : ", Multi(a, b))

if __name__ == "__main__":
    main()    