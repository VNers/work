def is_prime(num):
    """Function to check if a number is prime or not"""
    if num <= 1:
        return f"{num} is not a prime"
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return f"{num} is not a prime"
    return f"{num} is prime"

def prime_generator(n):
    """Generator function for prime numbers"""
    count = 0
    number = 2
    while count < n:
        if is_prime(number):
            yield number
            count += 1
        number += 1
