import string

def word_count(s):
    """
    Find the number of occurrences of each word
    in a string (excluding punctuation characters).
    """
    # Remove punctuation and convert to lowercase
    s = s.translate(str.maketrans("", "", string.punctuation)).lower()
    
    # Split the string into words and count occurrences
    word_list = s.split()
    word_count_dict = {}
    
    for word in word_list:
        if word in word_count_dict:
            word_count_dict[word] += 1
        else:
            word_count_dict[word] = 1
    
    return word_count_dict

def dict_items(d):
    """
    Return a list of all the items - (key, value) pair tuples - of the dictionary, `d`.
    """
    return list(d.items())

def dict_items_sorted(d):
    """
    Return a list of all the items - (key, value) pair tuples - of the dictionary, `d`
    sorted by `d`'s keys.
    """
    return sorted(d.items())

# Example usage:
sentence = "This is a sample sentence. Sample sentence for testing."
word_count_result = word_count(sentence)
print("Word count:", word_count_result)

dictionary = {'b': 2, 'a': 1, 'c': 3}
dict_items_result = dict_items(dictionary)
print("Dictionary items:", dict_items_result)

dict_items_sorted_result = dict_items_sorted(dictionary)
print("Dictionary items sorted:", dict_items_sorted_result)