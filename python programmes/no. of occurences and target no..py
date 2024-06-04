def count_occurrences(numbers, target):
    count = 0
    for num in numbers:
        if num == target:
            count += 1
    return count

# Example usage
numbers_tuple = (1, 2, 3, 4, 5, 2, 2, 3, 2)
target_number = int(input("Enter the target number: "))

occurrences = count_occurrences(numbers_tuple, target_number)
print(f"The target number {target_number} occurs {occurrences} times in the tuple.")
