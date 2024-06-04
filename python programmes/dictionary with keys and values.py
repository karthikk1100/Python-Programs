def print_dictionary(dictionary):
    """Function to print the contents of a dictionary"""
    for key, value in dictionary.items():
        print(f"{key} : {value}")

# Initialize the dictionary with keys and values
my_dict = {'apple': 5, 'orange': 10, 'banana': 12}

# Print the contents of the dictionary
print("Contents of the dictionary:")
print_dictionary(my_dict)
