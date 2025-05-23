"""
Accept a list of integers from the user and use the map() function to double each value.
"""

# def double_number(no):
#     return no + no

def main():
    no = int(input("Enter a number: "))
    lst = []
    for i in range(no):
        lst.append(int(input()))
    print("List of numbers:", lst)
    
    # Double_list = list(map(double_number, lst))
    Double_list = list(map(lambda no: no + no, lst))
    print("Doubled List:", Double_list)    

if __name__ == "__main__":
    main()    