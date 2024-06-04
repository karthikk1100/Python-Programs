def fahrenheit_to_celsius(fahrenheit):
    celsius = (5/9) * (fahrenheit - 32)
    return celsius

def main():
    # Taking input from the user
    fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
    
    # Converting Fahrenheit to Celsius
    celsius = fahrenheit_to_celsius(fahrenheit)
    
    # Displaying the converted temperature
    print("Temperature in Celsius:", celsius)

if __name__ == "__main__":
    main()
