from random import shuffle as random_shuffle
import os

def unique(items):
    """
    Return a set of unique values belonging to the `items` list
    """
    return set(items)

def shuffle(items):
    """
    Shuffle all items in a list
    """
    random_shuffle(items)
    return items

def getcwd():
    """
    Get current working directory
    """
    return os.getcwd()

def mkdir(name):
    """
    Create a directory at the current working directory
    """
    os.mkdir(name)
    return os.path.join(os.getcwd(), name)


sample_list = [1, 2, 3, 4, 5, 1, 2, 3]
unique_values = unique(sample_list)
print("Unique values:", unique_values)

shuffled_list = shuffle(sample_list.copy())
print("Shuffled list:", shuffled_list)

current_directory = getcwd()
print("Current working directory:", current_directory)

new_directory = mkdir("new_directory")
print("Created directory:", new_directory)