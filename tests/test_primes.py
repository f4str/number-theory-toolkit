from number_theory_toolkit import primes


def test_primes():
    assert not primes.is_prime(53531)
    assert not primes.is_prime(15765)
    assert primes.is_prime(18637)

    prime_nums = [2, 3, 5, 7, 11, 13, 17, 19, 23]
    assert primes.sieve_of_eratosthenes(25) == prime_nums

    assert all([primes.is_prime(p) for p in primes.sieve_of_eratosthenes(1000)])
