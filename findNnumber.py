import random

def quickselect_non_recursive(arr, left, right, k):
    while left <= right:
        pivot_index = random.randint(left, right)
        pivot_value = arr[pivot_index]

        arr[pivot_index], arr[right] = arr[right], arr[pivot_index]
        
        store_index = left
        for i in range(left, right):
            if arr[i] > pivot_value: 
                arr[store_index], arr[i] = arr[i], arr[store_index]
                store_index += 1

        arr[store_index], arr[right] = arr[right], arr[store_index]

        if k == store_index:
            return arr[k]
        elif k < store_index:
            right = store_index - 1
        else:
            left = store_index + 1

    return arr[left]

def find_number(numbers, which):
    numbers = [int(num) for num in numbers]
    unique_numbers = list(set(numbers))

    if len(unique_numbers) < which:
        return None
    
    return quickselect_non_recursive(unique_numbers, 0, len(unique_numbers) - 1, which - 1)

input_string = input('Enter your list of numbers (separated by space):\n') 
which = int(input("Which position number do you want to find (from highest to lowest)?\n"))

numbers = input_string.split()

result = find_number(numbers, which)

if result is not None:
    print(f"The number in position {which} (from highest) is: {result}")
else:
    print(f"The list doesn't contain {which} distinct numbers.")
