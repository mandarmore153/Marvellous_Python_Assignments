"""
Vowel or Consonant Check
Accept a single character from the user and check if it ia a vowel (a, e, i, o, u) or a consonant (b, c, d, f, g, h, j, k, l, m, n, p, q, r, s, t, v, w, x, y, z).
If not, print its a consonant.
"""
def ChkVowel(character):
    vowel = ['a', 'e', 'i', 'o', 'u']
    
    if character in vowel:
        print(f"'{character}' is a vowel.")
    else:
        print(f"'{character}' is a consonant.")    


def main():
    
    character = input("Enter a character: ")
    if len(character) == 1:
        ChkVowel(character)
    else:
        print("Please enter a single character.")    
    
if __name__ == "__main__":
    main()    