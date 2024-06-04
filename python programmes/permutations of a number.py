from itertools import permutations

def unique_permutations(num):
    # Convert the number to a list of digits
    digits = list(str(num))
    
    # Generate permutations of the digits
    perm_set = set(permutations(digits))
    
    # Convert permutations back to numbers and print them
    for perm in perm_set:
        print(int(''.join(perm)))

# Test the function with a given number
number = int(input("Enter a number: "))
print("Unique permutations of", number, "are:")
unique_permutations(number)
