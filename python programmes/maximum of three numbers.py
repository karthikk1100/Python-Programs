def main():
    try:
        num1, num2, num3 = map(int, input("Enter three numbers separated by space: ").split())
        maximum = max(num1, num2, num3)
        print("The maximum of the three numbers is:", maximum)
    except ValueError:
        print("Please enter valid integers separated by space.")

if __name__ == "__main__":
    main()
