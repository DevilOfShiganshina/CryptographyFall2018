from fractions import gcd
def MultMod(N):
	unitN = []
	for i in range (1, N):
		if gcd(i, N) == 1:
			unitN.append(i)
	size = len(unitN)
	table = [[0 for i in range(size)] for j in range(size)]
	for i in range (size):
		for j in range(size):
			table[i][j] = (unitN[i]*unitN[j]) % N
			print(table[i][j], " ", end='')
		print()
MultMod(10)
