"""
Accept a list of numbers and use reduce) (from functools)
to find the product of all numbers.
"""

from functools import reduce


# def product(no1, no2):
#     return no1 * no2
def main():
    no = int(input("Enter a number: "))
    lst = []
    for i in range(no):
        lst.append(int(input()))
    print("List of numbers:", lst)
    
    # Product =  reduce(product, lst)   
    
    Product = reduce(lambda no1, no2: no1 * no2, lst)
    
    print("Product:", Product)


if __name__ == "__main__":
    main()