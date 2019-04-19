def CompPower(base, exponent, mod):
	bs = bin(exponent)[2:]
	plist = []
	retval = 0
	power = 1
	for i in range (len(bs)):
		retval = (base**power) % mod
		plist.insert(0, retval)
		power *= 2
	retval = 1
	for i in range (len(bs)):
		if bs[i] == '1':
			retval *= plist[i]
	retval %= mod
	print(base, "^", exponent, " (mod ", mod, "): ", retval, sep='')
CompPower(14, 225, 53)
CompPower(14, 3939, 101)
