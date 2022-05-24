# decimal input and preprocessing
bits_str = input("Enter a binary: ")
bits_list = [int(bit) for bit in bits_str]

# store decimal quantity relative to each bit
decs = [bit*(2**pos) for pos, bit in enumerate(bits_list)]
# sum them all up
decimal = sum(decs)

print("decimal: ",decimal)