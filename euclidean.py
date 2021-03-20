def euclidean(a, b, verbose=False):
	if a < b:
		return euclidean(b, a, verbose)
	elif b == 0:
		if verbose:
			print(f'gcd = {a}')
		return a
	else:
		if verbose:
			print(f'{a} = {a // b} * {b} + {a % b}')
		return euclidean(b, a % b, verbose)


def bezout_coefficients(a, b, verbose=False, even=False):
	if a < b:
		return bezout_coefficients(b, a, verbose, not even)
	elif b == 0:
		if verbose:
			print(f'gcd = {a}')
		return 1, 0, a
	else:
		q = a // b
		r = a % b
		x, y, g = bezout_coefficients(b, r, verbose, not even)
		if verbose:
			if x != 0 and y != 0:
				if even:
					print(f'{g} = {x} * {b} + {y} * ({a} - {q} * {b})')
					print(f'{g} = {x - q * y} * {b} + {y} * {a}')
				else:
					print(f'{g} = {y} * ({a} - {q} * {b}) + {x} * {b}')
					print(f'{g} = {y} * {a} + {x - q * y} * {b}')
			elif y != 0:
				if even:
					print(f'{g} = {x - q * y} * {b} + {y} * {a}')
				else:
					print(f'{g} = {y} * {a} + {x - q * y} * {b}')
		return y, x - q * y, g


if __name__ == '__main__':
	print(euclidean(7245, 4784, True))
	print(bezout_coefficients(951, 456, True))
	