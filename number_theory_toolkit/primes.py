from typing import List


def is_prime(n: int) -> bool:
    if n <= 3:
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return False

    upper = int(n ** 0.5)
    for i in range(5, upper, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False

    return True


def sieve_of_eratosthenes(n: int) -> List[int]:
    primes = []
    not_primes = set()
    for i in range(2, n + 1):
        if i not in not_primes:
            primes.append(i)
            for j in range(i * i, n + 1, i):
                not_primes.add(j)
    return primes
