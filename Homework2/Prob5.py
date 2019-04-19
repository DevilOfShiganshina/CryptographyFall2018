def DiscreteLogarithm(base, remainder, mod):
	exponent = 0;
	retval = 0;
	for i in range(1, mod):
		retval = (base ** i) % mod 
		if retval == remainder:
			print("Exponent:", i)
			return
	print("No solution!")
DiscreteLogarithm(3, 19, 29)
DiscreteLogarithm(10, 32, 53)
