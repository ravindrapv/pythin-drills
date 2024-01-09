def sum_items_in_list(x):
    return sum(x)

def list_length(x):
    return len(x)

def last_three_items(x):
    return x[-3:]

def first_three_items(x):
    return x[:3]

def sort_list(x):
    return sorted(x)

def append_item(x, item):
    x.append(item)
    return x

def remove_last_item(x):
    if x:
        x.pop()
    return x

def count_occurrences(x, item):
    return x.count(item)

def is_item_present_in_list(x, item):
    return item in x

def append_all_items_of_y_to_x(x, y):
    x.extend(y)
    return x

def list_copy(x):
    return x.copy()

# Example usage:
sample_list = [1, 2, 3, 4, 5]
print("Original List:", sample_list)

print("Sum of items:", sum_items_in_list(sample_list))
print("Length of list:", list_length(sample_list))
print("Last three items:", last_three_items(sample_list))
print("First three items:", first_three_items(sample_list))

sorted_list = sort_list(sample_list)
print("Sorted list:", sorted_list)

append_item(sample_list, 6)
print("After appending 6:", sample_list)

remove_last_item(sample_list)
print("After removing last item:", sample_list)

print("Count of occurrences of 3:", count_occurrences(sample_list, 3))
print("Is 4 present in the list?", is_item_present_in_list(sample_list, 4))

another_list = [7, 8, 9]
append_all_items_of_y_to_x(sample_list, another_list)
print("After appending all items from another_list:", sample_list)

copied_list = list_copy(sample_list)
print("Shallow copy of the list:", copied_list)