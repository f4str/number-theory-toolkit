from number_theory_toolkit import binomial_coefficient, binomial_theorem, pascal_triangle


def test_binomial():
    assert binomial_coefficient(5, 2) == 10
    assert binomial_coefficient(5, 3) == 10
    assert binomial_coefficient(2, 1) == 2

    triangle = [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
    assert pascal_triangle(5) == triangle

    assert binomial_theorem(1, 2, 4) == 81

    poly1 = 'x^3 + 3 * x^2 * y + 3 * x * y^2 + y^3'
    poly2 = 'x^3 + 6 * x^2 + 12 * x + 8'
    poly3 = '125 + 75 * y + 15 * y^2 + y^3'
    assert binomial_theorem('x', 'y', 3) == poly1
    assert binomial_theorem('x', 2, 3) == poly2
    assert binomial_theorem(5, 'y', 3) == poly3

    poly4 = '1 * x^3 * y^0 + 3 * x^2 * y^1 + 3 * x^1 * y^2 + 1 * x^0 * y^3'
    assert binomial_theorem('x', 'y', 3, False) == poly4
