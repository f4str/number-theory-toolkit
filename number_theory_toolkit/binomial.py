import math
from typing import List, Union


def binomial_coefficient(n: int, k: int) -> int:
    if k <= 0 or k >= n:
        return 1
    if k == 1 or k == n - 1:
        return n
    b = math.factorial(n) / (math.factorial(k) * math.factorial(n - k))
    return int(b)


def pascal_triangle(n: int) -> List[List[int]]:
    triangle: List[List[int]] = []
    for _ in range(n):
        row = [1]
        if triangle:
            previous_row = triangle[-1]
            current_row = [sum(pair) for pair in zip(previous_row, previous_row[1:])]
            row.extend(current_row)
            row.append(1)
        triangle.append(row)
    return triangle


def binomial_theorem(
    x: Union[int, float, str], y: Union[int, float, str], n: int, trim=True
) -> Union[int, float, str]:
    if isinstance(x, (int, float)) and isinstance(y, (int, float)):
        total: Union[int, float] = 0
        for k in range(n + 1):
            coeff = binomial_coefficient(n, k) * (x ** (n - k)) * (y ** k)
            total += coeff
        return total
    else:
        terms: List[str] = []
        for k in range(n + 1):
            if trim:
                terms = []
                comb = binomial_coefficient(n, k)
                if comb > 1:
                    terms.append(str(comb))

                if n - k == 1:
                    terms.append(f'{x}')
                elif n - k > 1:
                    terms.append(f'{x}^{n - k}')

                if k == 1:
                    terms.append(f'{y}')
                elif k > 1:
                    terms.append(f'{y}^{k}')

                term = ' '.join(terms)
            else:
                term = f'{binomial_coefficient(n, k)} {x}^{n - k} {y}^{k}'
            terms.append(term)
        return ' + '.join(terms)
