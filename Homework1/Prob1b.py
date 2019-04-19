

def decrypt(c):

	a = 21
	b = 2
	x = a * (c - b)

	x = x % 26

	return x

list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

print("Ciphertext: A Plaintext:", list[decrypt(0)])
print("Ciphertext: B Plaintext:", list[decrypt(1)])
print("Ciphertext: C Plaintext:", list[decrypt(2)])
print("Ciphertext: D Plaintext:", list[decrypt(3)])
print("Ciphertext: E Plaintext:", list[decrypt(4)])
print("Ciphertext: F Plaintext:", list[decrypt(5)])
print("Ciphertext: G Plaintext:", list[decrypt(6)])
print("Ciphertext: H Plaintext:", list[decrypt(7)])
print("Ciphertext: I Plaintext:", list[decrypt(8)])
print("Ciphertext: J Plaintext:", list[decrypt(9)])
print("Ciphertext: K Plaintext:", list[decrypt(10)])
print("Ciphertext: L Plaintext:", list[decrypt(11)])
print("Ciphertext: M Plaintext:", list[decrypt(12)])
print("Ciphertext: N Plaintext:", list[decrypt(13)])
print("Ciphertext: O Plaintext:", list[decrypt(14)])
print("Ciphertext: P Plaintext:", list[decrypt(15)])
print("Ciphertext: Q Plaintext:", list[decrypt(16)])
print("Ciphertext: R Plaintext:", list[decrypt(17)])
print("Ciphertext: S Plaintext:", list[decrypt(18)])
print("Ciphertext: T Plaintext:", list[decrypt(19)])
print("Ciphertext: U Plaintext:", list[decrypt(20)])
print("Ciphertext: V Plaintext:", list[decrypt(21)])
print("Ciphertext: W Plaintext:", list[decrypt(22)])
print("Ciphertext: X Plaintext:", list[decrypt(23)])
print("Ciphertext: Y Plaintext:", list[decrypt(24)])
print("Ciphertext: Z Plaintext:", list[decrypt(25)])