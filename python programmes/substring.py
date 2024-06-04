def check_substring(string, substring):
    if substring in string:
        return "Substring found"
    else:
        return "Substring not found"

def main():
    input_string = input("Enter the string: ")
    substring = input("Enter the substring to check: ")
    result = check_substring(input_string, substring)
    print(result)

if __name__ == "__main__":
    main()
