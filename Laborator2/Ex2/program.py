def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def find_primes_in_list(numbers_to_check):
    primes_found = []
    for number in numbers_to_check:
        if is_prime(number):
            primes_found.append(number)
    return primes_found

number_to_check = input("Enter a list of numbers to check if they are prime: ")
numbers = list(map(int, number_to_check.split()))
primes = find_primes_in_list(numbers)
for prime in primes:
    print(prime, end=" ")