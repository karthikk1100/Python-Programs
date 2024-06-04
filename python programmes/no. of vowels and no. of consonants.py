def count_vowels_and_consonants(statement):
    vowels = sum(1 for char in statement if char.lower() in 'aeiou')
    consonants = sum(1 for char in statement if char.isalpha() and char.lower() not in 'aeiou')
    return vowels, consonants

# Taking input from the user
statement = input("Enter the statement: ")

# Counting the number of vowels and consonants
vowels_count, consonants_count = count_vowels_and_consonants(statement)

# Determining which count is maximum
max_category = "vowels" if vowels_count > consonants_count else "consonants" if consonants_count > vowels_count else "vowels and consonants"
max_count = max(vowels_count, consonants_count)

# Printing the results
print("Number of vowels =", vowels_count)
print("Number of consonants =", consonants_count)
print("The maximum count is for", max_category, "=", max_count)
