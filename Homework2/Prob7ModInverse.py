def Modular_Inverse(power, mod):
	MI = 0
	for i in range(mod):
		if (power*i) % mod == 1:
			MI = i
	print("Inverse of eq: x^", power, " (mod ", mod, "): ", MI, sep='')
Modular_Inverse(71, 2878)
