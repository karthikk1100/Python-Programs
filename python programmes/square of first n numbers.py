def sum_of_squares(n):
    return sum(i ** 2 for i in range(1, n + 1))

def main():
    try:
        n = int(input("Enter a positive integer N: "))
        if n < 0:
            print("Please enter a positive integer.")
        else:
            result = sum_of_squares(n)
            print("Sum of squares of first", n, "natural numbers is:", result)
    except ValueError:
        print("Please enter a valid integer for N.")

if __name__ == "__main__":
    main()
