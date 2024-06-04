def count_letters(string):
    return sum(char.isalpha() for char in string)

def main():
    input_string = input("Enter a string: ")
    num_letters = count_letters(input_string)
    print("Letters:", num_letters)

if __name__ == "__main__":
    main()
