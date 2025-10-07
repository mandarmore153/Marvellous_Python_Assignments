"""
Design python application which creates three threads as small, capital,digits.
All the theads accepts string as parameter. Small thread dispaly number of small characters,
capital thread display the number of capital characters and digit thread display number of digits.
Display id and name of each thread.

"""

import threading

def small(input_string):
    print("Thread name is small_thread")
    print("Thread ID of small_thread:", threading.get_ident())
    
    small_char = 0
    for char in input_string:
        if char.islower():
            small_char += 1
    print("Number of small characters:", small_char)        


def capital(input_string):
    print("Thread name is capital_thread")
    print("Thread ID of capital_thread:", threading.get_ident())
    
    capital_char = 0
    for char in input_string:
        if char.isupper():
            capital_char += 1
    print("Number of Capital characters:", capital_char) 

def digit(input_string):
    print("Thread name is digit_thread")
    print("Thread ID of digit_thread:", threading.get_ident())
    
    digit_char = 0
    for char in input_string:
        if char.isdigit():
            digit_char += 1
    print("Number of Digit characters:", digit_char)

def main():
    input_string = input("Enter a string: ")
    # input_string = "Marvellous123" 

    small_thread = threading.Thread(target=small, args=(input_string,))
    capital_thread = threading.Thread(target=capital, args=(input_string,))
    digit_thread = threading.Thread(target=digit, args=(input_string,))

    small_thread.start()
    capital_thread.start()
    digit_thread.start()

    small_thread.join()
    capital_thread.join()
    digit_thread.join()

    
if __name__ == "__main__":
    main()