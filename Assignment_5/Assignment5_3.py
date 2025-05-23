"""
Voting Eligibility Checker
Accept age from the user and check whether the person is eligible to vote.
(Age should be 18 or above)

"""

def ChkAge(age):
    if age >= 18:
        print("You are eligible to vote.")
    else:
        print("You are not eligible to vote.")


def main():
    age = int(input("Enter your age: "))
    
    ChkAge(age)
        
        
if __name__ == "__main__":
    main()    