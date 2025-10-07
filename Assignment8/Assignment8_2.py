"""
Design python application which creates two threads as evenfactor and oddfactor.
Both the thread accept one parameter as integer. Evenfactor thread will display
addition of given factors of given number and oddfactor will display addition of odd
factors of given number. After execution of both the thread gets completed main thread
should display message as "exit from main".
"""

import threading

def EvenFactor(no):
    even_factor = []
    for i in range(1, no + 1):        
        if no % i == 0:
            even_factor.append(i)    
    
    sum = 0
    for factor in even_factor:
        if factor % 2 == 0:
            sum += factor

    print(sum)        

def OddFactor(no):
    even_factor = []
    for i in range(1, no + 1):        
        if no % i == 0:
            even_factor.append(i)    
    
    sum = 0
    for factor in even_factor:
        if factor % 2 != 0:
            sum += factor

    print(sum)         

def main():
    number = int(input("Enter a number: "))   

    even_thread = threading.Thread(target=EvenFactor, args=(number,))
    odd_thread = threading.Thread(target=OddFactor, args=(number,))

    even_thread.start()
    odd_thread.start()

    even_thread.join()
    odd_thread.join()

    print("Exit from main")
    
if __name__ == "__main__":
    main()