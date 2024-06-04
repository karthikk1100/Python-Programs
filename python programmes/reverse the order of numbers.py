import array

def reverse_array(arr):
    return arr[::-1]

def main():
    original_array = array.array('i', [1, 3, 5, 3, 7, 1, 9, 3])
    print("Original array:", original_array)
    reversed_array = reverse_array(original_array)
    print("Reverse the order of the items:")
    print(reversed_array)

if __name__ == "__main__":
    main()
