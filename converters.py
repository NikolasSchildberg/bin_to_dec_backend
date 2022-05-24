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

def bin_to_dec(bits_str):
    """
    Converts a string representing a binary number to its decimal representation.
    
    Important:
        Expects a string as argument for the binary number.
        Returns a string containing the decimal representation.
    """
    # check argument type
    if type(bits_str) != str:
        raise TypeError("bin_to_dec() expects a string as argument")
    
    # check for invalid bits
    for bit in bits_str:
        if bit not in '01':
            raise ValueError('Binary argument must contain only "0"s and "1"s.')

    # extract bits from string
    bits_list = [int(bit) for bit in bits_str]

    # sort to convert from zero-th power to biggest power
    bits_list.reverse()

    # store decimal quantity relative to each bit
    decs = [bit*(2**pos) for pos, bit in enumerate(bits_list)]
    
    # sum all bits (decimal) values
    decimal = sum(decs)

    return(str(decimal))