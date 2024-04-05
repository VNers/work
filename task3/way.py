from code import is_prime, prime_generator

num = 23
if is_prime(num):
    print(f"{num} is prime")
else:
    print(f"{num} is not prime")


n = 15
for prime in prime_generator(n):
    print(prime)
