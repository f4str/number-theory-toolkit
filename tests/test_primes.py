from number_theory_toolkit import is_prime, sieve_of_eratosthenes


def test_primes():
    assert not is_prime(53531)
    assert not is_prime(15765)
    assert is_prime(18637)

    prime_nums = [2, 3, 5, 7, 11, 13, 17, 19, 23]
    assert sieve_of_eratosthenes(25) == prime_nums

    assert all([is_prime(p) for p in sieve_of_eratosthenes(1000)])
