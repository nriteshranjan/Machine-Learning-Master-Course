import math


def val(): return int(input().rstrip())


N = 1000000000
mxn = 1000002
sieve = [0] * mxn
pr = []

def calculateSieve():
	for i in range(2, mxn):
	    if sieve[i] == 0:
	        pr.append(i)
	        for j in range(i * i, mxn, i):
	            sieve[j] = i

def isPrime(n):
    if (n <= 1):
        return False
    if (n <= 3):
        return True
    if (n % 2 == 0 or n % 3 == 0):
        return False
    i = 5
    while(i * i <= n):
        if (n % i == 0 or n % (i + 2) == 0):
            return False
        i = i + 6
    return True

for _ in range(val()):
	m, n = input().split()
	m = int(m)
	n = int(n)
	for i in range(m, n + 1):
		if isPrime(i):
			print(i, end = " ")
	print()