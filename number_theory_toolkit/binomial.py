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
    x: Union[int, float, str], y: Union[int, float, str], n: int, simplify=True
) -> Union[int, float, str]:
    if simplify and isinstance(x, (int, float)) and isinstance(y, (int, float)):
        return (x + y) ** n
    else:
        terms: List[str] = []
        for k in range(n + 1):
            coefficient: float = binomial_coefficient(n, k)
            if simplify:
                term_list: List[str] = []

                if isinstance(x, (int, float)):
                    coefficient *= x ** (n - k)
                else:
                    if n - k == 1:
                        term_list.append(f'{x}')
                    elif n - k > 1:
                        term_list.append(f'{x}^{n - k}')

                if isinstance(y, (int, float)):
                    coefficient *= y ** k
                else:
                    if k == 1:
                        term_list.append(f'{y}')
                    elif k > 1:
                        term_list.append(f'{y}^{k}')

                if coefficient > 1:
                    term_list.insert(0, str(coefficient))

                term = ' * '.join(term_list)
            else:
                term = f'{coefficient} * {x}^{n - k} * {y}^{k}'

            terms.append(term)
        return ' + '.join(terms)
