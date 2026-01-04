"""
Write a program which contains filter(), map() and reduce() in it. Python application which contains one list of numbers.
List contains the numbers which accepted from user. Filter should filter out all such numbers whiich greater than or equal to 70 and less than or equal to 90.
Map function will increase each number by 10.Reduce will return product of all that numbers.
"""

from functools import reduce

def filterlist(no):
    if no >= 70 and no <= 90:
        return no
    
def AddedTen(no):
    return no + 10    

def Product(no1, no2):
    return no1 * no2

def main():
    no = int(input('Enter a number: '))

    input_list = []
    for i in range(no):
        num = int(input())
        input_list.append(num)

    filtered_output = list(filter(filterlist, input_list))
    print("List after filter :", filtered_output)

    map_output = list(map(AddedTen,filtered_output))
    print("List after map :", map_output)

    reduce_output = reduce(Product, map_output)
    print("List after reduce :", reduce_output)

if __name__ == "__main__":
    main()