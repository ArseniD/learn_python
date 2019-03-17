if __name__ == '__main__':
    print(b"This is OK because it's 7-bit ASCII")

    # To represent othe bytes with values equivalent to ASCII control codes and
    # byte values from 128 to 255 inclusive, we must use escape sequences with
    # \x (sequence of bytes - not just sequence of characters)
    print(b"Norwegian characters like \xc5 and \xd8 are not 7-bit ASCII")

    # If we want a sequence of the Unicode points we must decode the bytes into
    # a text sequence of the str type, and for this we need to know encoding.
    # latin1 for instance
    norsk = b"Norwegian characters like \xc5 and \xd8 are not 7-bit ASCII"
    print(norsk.decode('latin1'))

    # When we retrieve an item from the bytes Offline Bundle by indexing we get
    # an int object, not a 1-byte sequence. This another fundamental difference
    # between bytes and str.
    print(norsk[0])

    # Slicing a bytes objects, however, does return a new bytes object
    print(norsk[21:25])

    # There a few other forms of the bytes constructor it's good to be aware
    # of.
    # 1) we can create a 0 length byte sequence
    # 2) we can create a 0 field  sequence of bytes of a given length by passing a single integer to the
    # bytes constructor
    # 3) we can also pass an iterable series of integers
    print(bytes())
    print(bytes(5))
    print(bytes(range(65, 65+26)))

    # Ensure that value is non-negative and less than 256 to prevent a
    # ValueError been raised
    # Example: bytes([64, 244, 255, 511])
    # 1) one option, if we need to construct a bytes object by encoding a Unicode
    # str object is to use the two argument form of the bytes constructor,
    # which accept str as the first argument and the name of an encoding for
    # the secong
    # 2) finally, there's a class method, which is a named factory function for
    # creating a bytes object from as string consisting of concatenated,
    # two-digit hexadecimal numbers
    print(bytes('Norwegian characters Å and Ø', 'utf16'))
    print(bytes.fromhex('54686520717569636b2062726f776e20666f78'))

    # we can convert to hex from str in other direction by using generator
    # expsression, stipping the leading '0x' from each resulting string using
    # slicing
    print(''.join(hex(c)[2:] for c in b'The quick brown fox'))
