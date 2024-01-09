def last_3_characters(x):
    """
    Return the last 3 characters of the input string `x`
    """
    return x[-3:]

def first_10_characters(x):
    """
    Return the first 10 characters of the input string `x`
    """
    return x[:10]

def chars_4_through_10(x):
    """
    Return characters 4 through 10 (inclusive) of the input string `x`
    """
    return x[3:10]

def str_length(x):
    """
    Return the length of the input string `x`
    """
    return len(x)

def words(x):
    """
    Return a list of words from the input string `x`
    """
    return x.split()

def capitalize(x):
    """
    Capitalize the first letter of the input string `x`
    """
    return x.capitalize()

def to_uppercase(x):
    """
    Convert the input string `x` to uppercase
    """
    return x.upper()


sample_string = "Hello, World! This is an example string."

print("Last 3 characters:", last_3_characters(sample_string))
print("First 10 characters:", first_10_characters(sample_string))
print("Characters 4 through 10:", chars_4_through_10(sample_string))
print("String length:", str_length(sample_string))
print("Words in the string:", words(sample_string))
print("Capitalized string:", capitalize(sample_string))
print("Uppercase string:", to_uppercase(sample_string))