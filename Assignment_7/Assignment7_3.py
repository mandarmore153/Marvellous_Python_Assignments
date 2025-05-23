"""
Accept a list of numbers and use filter() to kepp only even numbers 
"""

# def even_number(no):
#     if no % 2 == 0:
#         return no

def main():
    no = int(input("Enter a number: "))
    lst = []
    for i in range(no):
        lst.append(int(input()))
    print("List of numbers:", lst)
    
    # Even_numbers = list(filter(even_number, lst))
    Even_numbers = list(filter(lambda no : no % 2 == 0 , lst))
    print("Even numbers :", Even_numbers)    

if __name__ == "__main__":
    main()  