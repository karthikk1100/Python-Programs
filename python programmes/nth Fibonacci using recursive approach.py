def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def main():
    try:
        n = int(input("Enter the value of N: "))
        if n < 0:
            print("Please enter a non-negative integer.")
        else:
            print("Fibonacci number at position", n, "is:", fibonacci(n))
    except ValueError:
        print("Please enter a valid integer for N.")

if __name__ == "__main__":
    main()
