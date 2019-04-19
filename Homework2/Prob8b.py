def isPrime(n):
	for i in range(2, n):
		if n % i == 0:
			return False
	return True
def Factors(n, fact):
	for i in range(2, n + 1):
		if n % i == 0:
			if(isPrime(i)):
				fact.append(i)
def EulersProductFormula(N):
	a = []
	Factors(N, a)
	#for i in range(len(a)):
	num = 1
	denom = 0
	product = 1
	for i in range(len(a)):
		denom = a[i]
		product *= 1 - (num / denom)
	product *= N
	print(int(product))
EulersProductFormula(96)
EulersProductFormula(245)
EulersProductFormula(936)
