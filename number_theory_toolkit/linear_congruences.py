from typing import List

from number_theory_toolkit import bezout_coefficients, euclidean_algorithm


def linear_congruence(a: int, b: int, n: int) -> List[int]:
    a, b = a % n, b % n

    d = euclidean_algorithm(a, n)
    if b % d != 0:
        return []

    a, b, n = a // d, b // d, n // d
    coeff = bezout_coefficients(a, n)[1] % n
    x = b * coeff % n
    return [x + i * n for i in range(d)]


def linear_congruence_system(a: int, b: int, n: int, m: int) -> int:
    if n < m:
        return linear_congruence_system(b, a, m, n)
    else:
        bezout = bezout_coefficients(n, m)
        e = bezout[0] * n
        f = bezout[1] * m
        x = b * e + a * f
        return x % (n * m)


def chinese_remainder_theorem(a: int, b: int, n: int, m: int) -> int:
    k = linear_congruence(n, b - a, m)[0]
    x = a + n * k
    return x % (n * m)
