from number_theory_toolkit.binomial import binomial_coefficient, binomial_theorem, pascal_triangle


def test_binomial():
    assert binomial_coefficient(5, 2) == 10
    assert binomial_coefficient(5, 3) == 10
    assert binomial_coefficient(2, 1) == 2

    triangle = [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
    assert pascal_triangle(5) == triangle

    assert binomial_theorem(1, 1, 4) == 16

    poly1 = 'y^4 + y^4'
    assert binomial_theorem('x', 'y', 4) == poly1
    poly2 = '1 x^4 y^0 + 4 x^3 y^1 + 6 x^2 y^2 + 4 x^1 y^3 + 1 x^0 y^4'
    assert binomial_theorem('x', 'y', 4, False) == poly2
