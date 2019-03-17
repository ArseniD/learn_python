if __name__ == '__main__':
    print(bytearray())
    print(bytearray(5))
    print(bytearray(b'Construct from a sequence of bytes'))
    print(bytearray('Norwegian characters Å and Ø', 'utf16'))
    print(bytearray.fromhex('54686520717569636b2062726f776e20666f78'))

    # Let's perform some operations on mutable object 'pangram'
    # The bytearray type supports the same operations as supported by list type
    # and bytes
    pangram = bytearray(b'The quick brown fox')
    print(pangram)
    pangram.extend(b' jumps over the lazy dog')
    print(pangram)
    pangram[40:43] = b'god'  # replace dog with god
    print(pangram)

    # Upper and lower make sense for 7-bit ASCII strings only
    print(pangram.upper())

    # Split our bytearray on white space, which returns a list of bytearray
    # object,and we can join that list of words back
    words = pangram.split()
    print(words)
    print(bytearray(b' ').join(words))

