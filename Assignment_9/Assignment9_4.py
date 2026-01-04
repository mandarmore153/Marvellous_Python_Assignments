
"""
Create a python program that Compare execution time of summing numbers from 1 to 10 
million using normal function, threading and  multiprocessing.
"""

import time
import threading
import multiprocessing

def NormalSum():

    sum = 0
    for i in range(1, 10000000):
        sum += i
    return sum

def thread_function():
    sum = 0
    for i in range(1, 10000000):
        sum += i
    return sum

def process_function():
    sum = 0
    for i in range(1, 10000000):
        sum += i
    return sum

def main():
    start_time = time.time()

    normal_sum = NormalSum()
    end_time = time.time()
    print("Sum of numbers from 1 to 10000000:", normal_sum)    
    print("Time taken for normal sum:", end_time - start_time,)

    start_time_t1 = time.time()
    t1 = threading.Thread(target=thread_function)
    t1.start()
    t1.join()
    end_time_t1 = time.time()
    print("Sum of numbers from 1 to 10000000 using thread:", thread_function())
    print("Time taken for threaded sum:", end_time_t1 - start_time_t1)

    start_time_p1 = time.time()

    p1 = multiprocessing.Process(target=process_function)
    p1.start()
    p1.join()
    end_time_p1 = time.time()
    print("Sum of numbers from 1 to 10000000 using process:", process_function())
    print("Time taken for process sum:", end_time_p1 - start_time_p1)


if __name__ == "__main__":
    main()
    