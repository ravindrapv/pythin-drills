def is_prime(n):
    """
    Check whether a number is prime or not.
    """
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def n_digit_primes(digit=2):
    """
    Return a list of `n_digit` primes using the `is_prime` function.
    Set the default value of the `digit` argument to 2.
    """
    if digit < 1:
        return []

    lower_limit = 10 ** (digit - 1)
    upper_limit = 10 ** digit - 1

    primes = [num for num in range(lower_limit, upper_limit + 1) if is_prime(num)]
    return primes


print("Is 7 prime?", is_prime(7)) 
print("Is 14 prime?", is_prime(14))  

two_digit_primes = n_digit_primes()
print(f"Two-digit primes: {two_digit_primes}")

three_digit_primes = n_digit_primes(digit=3)
print(f"Three-digit primes: {three_digit_primes}")