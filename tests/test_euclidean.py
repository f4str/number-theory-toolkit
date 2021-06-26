from number_theory_toolkit.euclidean import bezout_coefficients, euclidean_algorithm


def test_euclidean():
    assert euclidean_algorithm(7245, 4784) == 23
    assert bezout_coefficients(951, 456) == (-35, 73, 3)
