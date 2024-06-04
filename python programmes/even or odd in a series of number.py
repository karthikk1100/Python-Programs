def count_even_odd(numbers):
    even_count = 0
    odd_count = 0

    for num in numbers:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    return even_count, odd_count

input_str = input("Enter a series of numbers separated by spaces: ")
numbers = tuple(map(int, input_str.split()))

even, odd = count_even_odd(numbers)
print("Number of even numbers:", even)
print("Number of odd numbers:", odd)
