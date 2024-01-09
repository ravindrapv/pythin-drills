def read_file(path):
    """
    Read and return the content of the file at the specified path.
    """
    try:
        with open(path, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        return f"File not found at path: {path}"
    except Exception as e:
        return f"Error reading file: {e}"

def write_to_file(path, s):
    """
    Write the given string to a new file at the specified path.
    """
    try:
        with open(path, 'w') as file:
            file.write(s)
    except Exception as e:
        print(f"Error writing to file: {e}")

def append_to_file(path, s):
    """
    Append the given string to an existing file at the specified path.
    """
    try:
        with open(path, 'a') as file:
            file.write(s)
    except Exception as e:
        print(f"Error appending to file: {e}")

def numbers_and_squares(n, file_path):
    """
    Save the first `n` natural numbers and their squares into a file in the csv format.
    """
    try:
        with open(file_path, 'w') as file:
            for i in range(1, n + 1):
                file.write(f"{i},{i*i}\n")
    except Exception as e:
        print(f"Error writing numbers_and_squares to file: {e}")

# Example usage:
write_to_file("example.txt", "Hello, this is a test.")
content = read_file("example.txt")
print("File content after writing:", content)

append_to_file("example.txt", "\nThis is an appended line.")
content_after_append = read_file("example.txt")
print("File content after appending:", content_after_append)

numbers_and_squares(3, "numbers.csv")
numbers_and_squares_content = read_file("numbers.csv")
print("File content for numbers_and_squares:", numbers_and_squares_content)