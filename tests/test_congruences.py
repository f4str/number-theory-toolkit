from number_theory_toolkit import (
    chinese_remainder_theorem,
    linear_congruence,
    linear_congruence_system,
)


def test_congruences():
    assert linear_congruence(2, 1, 5) == [3]
    assert linear_congruence(2, 1, 6) == []
    assert linear_congruence(7, 4, 25) == [22]
    assert linear_congruence(15, 10, 25) == [4, 9, 14, 19, 24]

    assert linear_congruence_system(2, 3, 4, 25) == 78
    assert linear_congruence_system(4, 2, 15, 8) == 34

    assert chinese_remainder_theorem(2, 3, 4, 25) == 78
    assert chinese_remainder_theorem(4, 2, 15, 8) == 34
