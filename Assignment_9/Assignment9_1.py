"""
Create a python program that starts 3 threads, each printing numbers 
from 1 to 5 with  a delay of 1 second. Use the threading.Thread.
"""

import threading
import time

def Display_Number():
    
    for i in range(1, 6):
        time.sleep(1)
        print(i, end=' ')


def main():

    t1 = threading.Thread(target=Display_Number)
    t2 = threading.Thread(target=Display_Number)
    t3 = threading.Thread(target=Display_Number)

    t1.start()
    t2.start()
    t3.start()
    
    t1.join()
    t2.join()
    t3.join()

if __name__ == "__main__":
    main()
        