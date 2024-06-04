def sum_of_list(numbers):
    
    total = 0
    
    for num in numbers:
        total += num
    return total


numbers = input("Enter the list of numbers separated by spaces: ").split()

numbers = [int(num) for num in numbers]


print("Sum of all numbers in the list:", sum_of_list(numbers))
