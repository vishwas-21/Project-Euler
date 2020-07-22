import time, math

t0 = time.time()
def gcd(a, b):
	if a % b == 0:
		return b
	return gcd(b, a % b)

tria = [0] * 1500001
for m in range(2, int(math.sqrt(1500000 // 2))):	# This is Because 1500000 = 2 * m * (m + _)
	n = 1
	l = 2 * m * (m + n)
	while 2 * m * (m + n) <= 1500000 and n < m:
		l = 2 * m * (m + n)
		if gcd(m, n) == 1 and (m + n) % 2 == 1:	# This is because they form primary pythagorean Triplets
			k = 1
			while k * l <= 1500000:
				tria[k * l] += 1
				k += 1
		n += 1
print("Answer is", tria.count(1))
print(time.time() - t0)
