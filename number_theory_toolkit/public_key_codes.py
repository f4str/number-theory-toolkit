from number_theory_toolkit.euclidean import bezout_coefficients


def encode(t: int, e: int, M: int) -> int:
    return pow(t, e, M)


def decode(s: int, e: int, M: int, K: int) -> int:
    d = bezout_coefficients(e, K)[1]
    return pow(s, d, M)


if __name__ == '__main__':
    p = 179424673
    q = 181329481
    M = p * q
    K = (p - 1) * (q - 1)
    e = 7919
    t = 133

    s = encode(t, e, M)
    print(s)
    print(decode(s, e, M, K))
