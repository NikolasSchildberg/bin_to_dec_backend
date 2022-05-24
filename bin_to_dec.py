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