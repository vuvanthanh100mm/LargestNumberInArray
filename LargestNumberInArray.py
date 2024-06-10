def find_largest_number(arr):
    # Ensure the array is not empty
    if not arr:
        raise ValueError("The array is empty")

    # Initialize the largest number with the first element
    largest = arr[0]

    # Iterate through the array and update the largest number
    for number in arr:
        if number > largest:
            largest = number

    return largest


# Example usage:
example_array = [10, 24, 159, 98, 73, 45]
print(find_largest_number(example_array))  # Output: 98
