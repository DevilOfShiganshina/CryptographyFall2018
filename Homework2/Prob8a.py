def Modular_Inverse(n, p):
	MI = 0
	for i in range(p):
		if (n*i) % p == 1:
			MI = i;
	return MI
def ChineseRemainderTheorem(val1, prime1, val2, prime2, val3, prime3):
	a1 = val1
	a2 = val2
	a3 = val3
	m1 = prime1
	m2 = prime2
	m3 = prime3
	MOD = m1 * m2 * m3
	M1 = MOD//m1
	M2 = MOD//m2
	M3 = MOD//m3
	invM1 = Modular_Inverse(M1, m1)
	invM2 = Modular_Inverse(M2, m2)
	invM3 = Modular_Inverse(M3, m3)
	X = (((a1* M1 * invM1) + (a2* M2 * invM2) + (a3 * M3 * invM3)) % MOD)
	print("CHINESE REMAINDER THEOREM")
	print("X =",X)
ChineseRemainderTheorem(34, 43, 2, 97, 20, 29)
