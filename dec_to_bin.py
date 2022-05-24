def dec_to_bin(dec_str):
    """
    Converts a string representing a decimal number to its binary representation.
    
    Important:
        Expects a string as argument for the decimal number.
        Returns a string containing the binary representation.
    """
    # check argument type
    if type(dec_str) != str:
        raise TypeError("dec_to_bin() expects a string as argument")

    # check for invalid digits
    for char in dec_str:
        if char not in '0123456789':
            raise ValueError('Decimal argument must contain only decimal digits.')

    # auxiliary variables for conversion
    current = int(dec_str)
    bits = []

    # calculating and storing each bit into "bits" list
    while (current > 1):
        bits.append(current%2)
        current = current//2

    # stores last remainder too, after loop
    bits.append(current)

    bits.reverse()
    bits = [str(bit) for bit in bits]
    bin_str = ''.join(bits)

    return bin_str