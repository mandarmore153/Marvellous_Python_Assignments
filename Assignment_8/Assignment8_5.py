""" 
Design python application which contains two threads named as thread1 and thread2.
Thread1 display 1 to 50 on screen and thread2 display 50 to 1 on reverse order on screen.
After execution of thread1 gets completed then schedule thread2.
"""

import threading


def Thread1():
    print("Thread1")
    for i in range(1, 50+1):
        print(i, end=' ')

def Thread2():
    print("\nThread2")
    for i in range(50,0,-1):
        print(i, end=' ')

def main():

    thread1 = threading.Thread(target=Thread1)
    thread2 = threading.Thread(target=Thread2)

    thread1.start()
    thread1.join()

    thread2.start()    
    thread2.join()

if __name__ == "__main__":
    main()    