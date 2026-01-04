"""
Write a program which contains filter(), map() and reduce() in it. Python application which contains one list of numbers.
List contains the numbers which accepted from user. Filter should filter out al prime numbers. Map function will multiply each number by 2.
Reduce will return maximum number from that numbers.
"""

from functools import reduce

def PrimeNo(no):
    prime_no = True
    for i in range(2, no):
        if no % i == 0:
            prime_no = False

    if prime_no == True:
        return no        
        
    
def Multiplication(no):
    return no * 2   

def MaxNo(no1, no2):
    return max(no1, no2)

def main():
    no = int(input('Enter a number: '))

    input_list = []
    for i in range(no):
        num = int(input())
        input_list.append(num)

    filtered_output = list(filter(PrimeNo, input_list))
    print("List after filter :", filtered_output)

    map_output = list(map(Multiplication,filtered_output))
    print("List after map :", map_output)

    reduce_output = reduce(MaxNo, map_output)
    print("List after reduce :", reduce_output)

if __name__ == "__main__":
    main()