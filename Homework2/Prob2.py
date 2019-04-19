from fractions import gcd
def Phi(n):
	count = 0;
	for i in range (1, n):
		if gcd(i, n) == 1:
			count += 1
	print("Phi(", n, ") is: ", count, sep='')
Phi(8712)
Phi(4794327)
