from number_theory_toolkit.public_key_codes import decode, encode


def test_binomial():
    p = 179424673
    q = 181329481
    M = p * q
    K = (p - 1) * (q - 1)
    e = 7919
    t = 133

    s = encode(t, e, M)
    assert s == 19756252527363215
    assert decode(s, e, M, K) == t
