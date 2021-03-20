def is_prime(n):
	if n <= 3:
		return n > 1
	if n % 2 == 0 or n % 3 == 0:
		return False
	
	upper = int(n ** 0.5)
	for i in range(5, upper, 6):
		if n % i == 0 or n % (i + 2) == 0:
			return False
	
	return True


def sieve_of_eratosthenes(n):
	primes = []
	not_primes = set()
	for i in range(2, n + 1):
		if i not in not_primes:
			primes.append(i)
			for j in range(i * i, n + 1, i):
				not_primes.add(j)
	return primes


if __name__ == '__main__':
	print(is_prime(53531))
	print(is_prime(15765))
	print(is_prime(18637))
	
	print(sieve_of_eratosthenes(100))
	
	print(all([is_prime(p) for p in sieve_of_eratosthenes(1000)]))
