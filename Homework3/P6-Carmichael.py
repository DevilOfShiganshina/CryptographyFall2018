def Carmichael(num):

    base = 0

    for i in range(num):
        if (base**num) % num != base:
            return False;
        base += 1
    return True

print("This proggram will determine if a specified integer is a Carmichael number!")
input = int(input("Please enter the integer: "))

if Carmichael(input) == True:
    print(input, "is a Carmichael number!")

else:
    print(input, "is not a Carmichael number!")