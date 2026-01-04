"""
Write a python program using multiprocessing. Process to squre a list of 
numbers using the multiple processes
"""

import multiprocessing

def Square(input_list):
    for i in input_list:
        print(i ** 2)   


def main():
    
    input_list = [1, 2, 3, 4, 5]
    p1 = multiprocessing.Process(target=Square, args=(input_list,))
    
    p1.start()
    p1.join()


if __name__ == "__main__":
    main()
      