def count_digits(number):
    return len(str(number))

def main():
    # Taking input from the user
    number = int(input("Enter number: "))
    
    # Counting the digits
    digit_count = count_digits(number)
    
    # Displaying the result
    print("Number of digits:", digit_count)

if __name__ == "__main__":
    main()
