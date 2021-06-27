from number_theory_toolkit import bezout_coefficients


def encode_key_code(t: int, e: int, M: int) -> int:
    return pow(t, e, M)


def decode_key_code(s: int, e: int, M: int, K: int) -> int:
    d = bezout_coefficients(e, K)[1]
    return pow(s, d, M)
