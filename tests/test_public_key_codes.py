from number_theory_toolkit import decode_key_code, encode_key_code


def test_binomial():
    p = 179424673
    q = 181329481
    M = p * q
    K = (p - 1) * (q - 1)
    e = 7919
    t = 133

    s = encode_key_code(t, e, M)
    assert s == 19756252527363215
    assert decode_key_code(s, e, M, K) == t
