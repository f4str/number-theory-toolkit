import math


def binomial_coefficient(n, k):
	if k <= 0 or k >= n:
		return 1
	if k == 1 or k == n - 1:
		return n
	b = math.factorial(n) / (math.factorial(k) * math.factorial(n - k))
	return int(b)


def pascal_triangle(n):
	triangle = []
	for i in range(n):
		row = [1]
		if triangle:
			previous_row = triangle[-1]
			current_row = [sum(pair) for pair in zip(previous_row, previous_row[1:])]
			row.extend(current_row)
			row.append(1)
		triangle.append(row)
	return triangle


def binomial_theorem(x, y, n, trim=True):
	if type(x) == type(y) == int:
		result = 0
		for k in range(n + 1):
			term = binomial_coefficient(n, k) * (x ** (n - k)) * (y ** k)
			result += term
		return result
	else:	
		result = []
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
			result.append(term)
		return ' + '.join(result)
		

if __name__ == '__main__':
	print(binomial_coefficient(5, 2))
	print(binomial_coefficient(5, 3))
	print(binomial_coefficient(2, 1))
	
	print(pascal_triangle(5))
	
	print(binomial_theorem(1, 1, 4))
	print(binomial_theorem('x', 'y', 4))
	print(binomial_theorem('x', 'y', 4, False))