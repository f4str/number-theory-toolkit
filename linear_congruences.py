from euclidean import euclidean, bezout_coefficients


def linear_congruence(a, b, n):
	a, b = a % n, b % n
	
	d = euclidean(a, n)
	if b % d != 0:
		return []
	
	a, b, n = a // d, b // d, n // d
	coeff = bezout_coefficients(a, n)[1] % n
	x = b * coeff % n
	return [x + i * n for i in range(d)]


def linear_congruence_system(a, b, n, m):
	if n < m:
		return linear_congruence_system(b, a, m, n)
	else:
		bezout = bezout_coefficients(n, m)
		e = bezout[0] * n
		f = bezout[1] * m
		x = b * e + a * f
		return x % (n * m)

def chinese_remainder(a, b, n, m):
	k = linear_congruence(n, b - a, m)[0]
	x = a + n * k
	return x % (n * m)


if __name__ == '__main__':
	print(linear_congruence(2, 1, 5))
	print(linear_congruence(2, 1, 6))
	print(linear_congruence(7, 4, 25))
	print(linear_congruence(15, 10, 25))
	
	print(linear_congruence_system(2, 3, 4, 25))
	print(linear_congruence_system(4, 2, 15, 8))
	
	print(chinese_remainder(2, 3, 4, 25))
	print(chinese_remainder(4, 2, 15, 8))
		