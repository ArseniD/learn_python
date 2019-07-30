if __name__ == "__main__":
    a = 60            # 60 = 0011 1100
    b = 13            # 13 = 0000 1101
    c = 0

    # & Binary AND
    # Operator copies a bit to the result if it exists in both operands
    c = a & b        # 12 = 0000 1100
    print("Line 1 - Value of c is ", c)

    # | Binary OR
    # It copies a bit if it exists in either operand.
    c = a | b        # 61 = 0011 1101
    print("Line 2 - Value of c is ", c)

    # ^ Binary XOR
    # It copies the bit if it is set in one operand but not both.
    c = a ^ b        # 49 = 0011 0001
    print("Line 3 - Value of c is ", c)

    # ~ Binary Ones Complement
    # Returns the complement of x - the number you get by switching
    # each 1 for a 0 and each 0 for a 1.
    # This is the same as -x - 1.
    c = ~a           # -61 = 1100 0011
    print("Line 4 - Value of c is ", c)

    # << Binary Left Shift
    # The left operands value is moved left by the number of bits specified by
    # the right operand.
    c = a << 2       # 240 = 1111 0000
    print("Line 5 - Value of c is ", c)

    # >> Binary Right Shift
    # The left operands value is moved right by the number of bits specified by
    # the right operand.
    c = a >> 2       # 15 = 0000 1111
    print("Line 6 - Value of c is ", c)

    # 0b - binary prefix
    print(0b11110000)
    print(bin(240))

    # 11100100
    #   XOR
    # 00100111
    #    =
    # 11000011
    print(bin(0b11100100 ^ 0b00100111))

    #  11110000 - 0b11110000
    #         not
    #  00001111 - 0b1111
    # -0b11110001
    print(bin(~0b11110000))

    # When we print negative numbers in binary Python actually uses a leading
    # unary minus with magnitude representation, rather than gibing unsigned
    # binary Two's Complement representations. We don't see easily get to see
    # the internal bit representation of negative numbers using bin.In fact, we
    # can't determine what internal representation scheme is used.
    print(bin(4))
    print(bin(-4))

    # Specify how many bit we want to represent by using bitwise AND & operand
    # with a mask (8-bit) of ones to discard all the leading ones in negative results.
    # 8 bits representation in result to be presented
    print(~0b11110000 & 0b11111111)

    # 9 bits representation in result to be presented
    print(~0b11110000 & 0b111111111)

    # We can ask Python how many bits are required to represent the interger
    # value using bit_length method of the integer type, although note that
    # this excludes the sign.
    print(int(32).bit_length())
    print(int(240).bit_length())
    print(int(-240).bit_length())
    print(int(256).bit_length())

    # Byte oriented representation directly as a bytes object using 2 bytes
    # method. Specify how many bytes we want in result by the length parameter
    # and byte order parameter whether we want bytes in big endian order with
    # the most significant byte first or little endian order with the least
    # sifnificant byte first.
    print(int(0xcafebabe).to_bytes(length=4, byteorder='big'))
    print(int(0xcafebabe).to_bytes(length=4, byteorder='little'))

    # Use native byte sort of your machine
    import sys
    print(sys.byteorder)
    little_cafebabe = int(0xcafebabe).to_bytes(length=4, byteorder=sys.byteorder)
    print(little_cafebabe)

    # Back into integer
    data = int.from_bytes(little_cafebabe, byteorder=sys.byteorder)
    print(data)
    # Convert to hex we started with
    print(hex(data))

    # Two's complement representations, by indexing into the result bytes
    # object to retrieve the least signigicant byte, and converting that to a
    # binary representation, although concise, this is not.
    print(int(-241).to_bytes(2, byteorder='little', signed=True))
    print(bin((~0b11110000).to_bytes(2, byteorder='little', signed=True)[0]))
