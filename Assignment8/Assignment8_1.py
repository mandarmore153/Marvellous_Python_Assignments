"""
Design python application which creates two thread neamed as even and odd. 
Even thread will display first 10 even numbers and odd thread will display first 10 odd numbers.

"""


import threading

def EvenThread(no):
    for i in range(no):
        if i % 2 == 0:
            print(i)

def OddThread(no):
    for i in range(no):
        if i % 2 != 0:
            print(i)            

def main():
    number = 10
    even_thread = threading.Thread(target=EvenThread, args=(number,))
    odd_thread = threading.Thread(target=OddThread, args=(number,))

    even_thread.start()
    odd_thread.start()

    even_thread.join()
    odd_thread.join()

    
    
if __name__ == "__main__":
    main()


