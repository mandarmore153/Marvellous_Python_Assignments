"""
Celsius to Fahrenheit Converter
Accept temperature in celsius and convert it to Fahrenheit using formula:
F = (C * 9/5) + 32

"""

def Feh(celsius):
    return (celsius * 9/5) + 32


def main():
    celsius = int(input("Enter temperature in celsius : "))
    
    result = Feh(celsius)
    
    print(f"Temperature in Fahrenheit  : {result}°F")
        
        
if __name__ == "__main__":
    main() 