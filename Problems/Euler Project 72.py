import time, math

t0 = time.time()
def gcd(a, b):
	if a % b == 0:
		return b
	return gcd(b, a % b)


def SieveOfEratosthenes(n):		# For finding primes
	primes = [True] * (n + 1)
	primes[0] = primes[1] = False
	for i in range(2, int(math.sqrt(n)+1)):
		if primes[i]:
			k = i
			while k * i <= n:
				primes[k * i] = False
				k += 1
	return primes

n = 1000000
primes = SieveOfEratosthenes(n)
totient = [0] * (n+1)	# Using euler totient function
totient[1] = 1
for num in range(2, n + 1):
	if primes[num]:
		totient[num] = num - 1
	else:
		i = 2
		temp = num
		while True:
			while temp % i == 0:
				temp //= i
			if temp != num:
				break
			i += 1
		if temp == 1:
			totient[num] = (num // i) * (i - 1)
		else:
			totient[num] = totient[num // temp] * totient[int(temp)]
print(sum(totient)-1)
print(time.time() - t0)