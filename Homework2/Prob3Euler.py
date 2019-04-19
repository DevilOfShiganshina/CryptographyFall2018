from fractions import gcd
def Phi(n):
	count = 0
	for i in range (1, n):
		if gcd(i, n) == 1:
			count += 1
	return count
def EulerTheorem(base, power, mod):
	phiOfmod = Phi(mod)
	remainder = power % phiOfmod
	answer = (base**remainder) % mod
	print(base, "^", power, " (mod ", mod, "): ", answer, sep='')
EulerTheorem(14, 225, 53)
EulerTheorem(14, 3969, 101)
