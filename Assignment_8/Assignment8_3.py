"""
Design python application which creates two threads as evenlist and oddlist.
Both the threads accept list of integers as parameter. Evenlist thread add all even elements
from input list and display the addition. Oddlist thread add all odd elements from input list
and display the addition.
"""

import threading

def EvenList(lst):
    Addition = 0
    for i in lst:
        if i % 2 == 0:
            Addition += i
    print("Addition of even numbers:", Addition)        

        
def OddList(lst):
    Addition = 0
    for i in lst:
        if i % 2 != 0:
            Addition += i
    print("Addition of odd numbers:", Addition) 


def main():
    input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]   

    even_thread = threading.Thread(target=EvenList, args=(input_list,))
    odd_thread = threading.Thread(target=OddList, args=(input_list,))

    even_thread.start()
    odd_thread.start()

    even_thread.join()
    odd_thread.join()

    
if __name__ == "__main__":
    main()