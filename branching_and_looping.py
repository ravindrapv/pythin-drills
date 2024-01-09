def integers_from_start_to_end_using_range(start, end, step):
    """
    Return a list of integers from start to end (inclusive) using the range function.
  
    """
    return list(range(start, end + 1, step))


def integers_from_start_to_end_using_while(start, end, step):
    """
    Return a list of integers from start to end (inclusive) using a while loop.
  
    """
    result = []
    current = start
    while current <= end:
        result.append(current)
        current += step
    return result


def two_digit_primes():
    """
    Return a list of all two-digit primes.
    """
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    return [num for num in range(10, 100) if is_prime(num)]

# Example usage
range_result = integers_from_start_to_end_using_range(1, 10, 2)
print("Using range:", range_result)

while_result = integers_from_start_to_end_using_while(1, 10, 2)
print("Using while loop:", while_result)

two_digit_primes_result = two_digit_primes()
print("Two-digit primes:", two_digit_primes_result)
