# decimal input
dec = int(input("Enter a decimal"))

# auxiliary variables
current = dec
bits = []

# storing each bit in bits list
while (current > 1):
    bits.append(current%2)
    current = current//2

bits.append(current) # last remainder, after loop

bits_str = ''
le = len(bits)
for i in range(le):
    bits_str += str(bits[le-i-1])

print('Bits string:', bits_str)