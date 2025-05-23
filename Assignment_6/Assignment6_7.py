"""
Accept 5 numbers from the user.Find and prit the lagest number. 
"""

def main():
    print("Enter 5 numbers : ")
    no = []
    for i in range(5):
        no.append(int(input()))
    
    print("maximum number is : ", max(no))
    

if __name__ == "__main__":
    main()    