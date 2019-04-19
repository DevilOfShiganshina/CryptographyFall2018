from fractions import gcd
def Phi(N):
	count = 0
	for i in range(1, N):
		if gcd(i, N) == 1:
			count += 1
	return count
def isPrime(N):
	for i in range(2, N):
		if N%i == 0:
			return False
	return True
def Output(order, Divisors, prime):
	for i in range(len(Divisors)):
			if (order**Divisors[i]) % prime == 1:
				print("Order of ", order, " in U(", prime, ") is: ", Divisors[i], sep='')
				return
def ComputeDivisors(N, divisors):
	for i in range(2, N):
		if N%i == 0:
			divisors.append(i)
def ComputeOrder(order, prime):
	Divisors = []
	if(isPrime(prime)):
		PhiVal = prime - 1
		ComputeDivisors(PhiVal, Divisors)
		Output(order, Divisors, prime)
	else:
		PhiVal = Phi(prime)
		ComputeDivisors(PhiVal, Divisors)
		Output(order, Divisors, prime)
ComputeOrder(16, 199)