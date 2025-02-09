def bubble_sort_dict(input_dict):
    # Convert dictionary to a list of tuples (key, value)
    items = list(input_dict.items())
    
    # Bubble sort algorithm
    n = len(items)
    for i in range(n):
        for j in range(0, n-i-1):
            # Swap if the value of the current item is greater than the next item
            if items[j][1] > items[j+1][1]:
                items[j], items[j+1] = items[j+1], items[j]
    
    # Convert the sorted list of tuples back to a dictionary
    sorted_dict = dict(items)
    return sorted_dict

# Example dictionary
my_dict = {"a": 3, "b": 1, "c": 4, "d": 2}

# Sort the dictionary by its values using Bubble Sort
sorted_dict = bubble_sort_dict(my_dict)
print(sorted_dict)
