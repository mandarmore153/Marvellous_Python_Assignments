"""
Create a Python program that uses multiprocessing.Pool to compute factorial of numbers in a lists. 
"""

import multiprocessing

def Factorial(input_list):
    fact = 1
    for i in range (1,input_list+1):
        fact *= i
        
    return fact     


def main():
    
    input_list = [1, 2, 3, 4, 5]
    result = []

    p = multiprocessing.Pool()
    result = p.map(Factorial, input_list)
    p.close()    
    p.join()

    print("Factorials:", result)

if __name__ == "__main__":
    main()
      