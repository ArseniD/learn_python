import mmap
# import struct
import code

from pprint import pprint as pp
from binascii import hexlify


# class Vector:

#     def __init__(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z

#     def __repr__(self):
#         return 'Vector({}, {}, {})'.format(self.x, self.y, self.z)


class Vector:

    def __init__(self, mem_float32):
        # we are expects expose floats
        # validate this by memoryview '.format' attribute,
        # string containing 'f' and 'd'
        if mem_float32.format not in "fd":
            raise TypeError(
                "Vector: memoryview values must be floating-point numbers")
        # check that memoryview exposes at least three items
        # len(memoryview) given number of items - not necessarily bytes if cast
        # has been used
        if len(mem_float32) < 3:
            raise TypeError(
                "Vector: memoryview must contain at least 3 floats")
        # mem holds the reference to the memory view
        self._mem = mem_float32

    # read only property
    @property
    def x(self):
        return self._mem[0]

    # read only property
    @property
    def y(self):
        return self._mem[1]

    # read only property
    @property
    def z(self):
        return self._mem[2]

    def __repr__(self):
        return 'Vector({}, {}, {})'.format(self.x, self.y, self.z)


# class Color:

#     def __init__(self, red, green, blue):
#         self.red = red
#         self.green = green
#         self.blue = blue

#     def __repr__(self):
#         return 'Color({}, {}, {})'.format(self.red, self.green, self.blue)


class Color:

    def __init__(self, mem_unit16):
        # we are expects expose floats
        # validate this by memoryview '.format' attribute,
        # string containing 'HILQ'
        if mem_unit16.format not in "HILQ":
            raise TypeError(
                "Color: memoryview values must be unsigned integers")
        # check that memoryview exposes at least three items
        # len(memoryview) given number of items - not necessarily bytes if cast
        # has been used
        if len(mem_unit16) < 3:
            raise TypeError(
                "Color: memoryview must contain at least 3 floats")
        # mem holds the reference to the memory view
        self._mem = mem_unit16

    # read only property
    @property
    def red(self):
        return self._mem[0]

    # read only property
    @property
    def green(self):
        return self._mem[1]

    # read only property
    @property
    def blue(self):
        return self._mem[2]

    def __repr__(self):
        return 'Vector({}, {}, {})'.format(self.red, self.green, self.blue)


class Vertex:

    def __init__(self, vector, color):
        self.vector = vector
        self.color = color

    def __repr__(self):
        return 'Vertex({!r}, {!r})'.format(self.vector, self.color)


# def make_colored_vertex(x, y, z, red, green, blue):
#     """
#     A factory function to construct instances of the type vertex,
#     which aggregate a vector and a color.

#     returns: a tuple of data
#     """
#     return Vertex(Vector(x, y, z),
#                   Color(red, green, blue))


def make_colored_vertex(mem_vertex):
    """
    The function slices the vertex memory view into two parts for the vector
    and color respectively, and casts each to a typed memory view.
    These are used to construct the vector and color objects., which are then
    passed on to the vertex constructor.
    """
    mem_vector = mem_vertex[0:12].cast('f')
    mem_color = mem_vertex[12:18].cast('H')
    return Vertex(Vector(mem_vector), Color(mem_color))


def main():
    # read file in binary mode
    with open('colors.bin', 'rb') as f:
        # retrieve the file handle or descriptor, passing it to the mmap
        # constructor.
        with mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ) as buffer:
            # read entire contents of the file into bytes object
            # buffer = f.read()

            # buffer now is a memory map file rather than the byte sequence, as
            # it was previously. We've avoided reading the file into memory
            # twice; once into the OS maintained file cache, and again, into
            # our own collection by directly working in the operating systems
            # view of the file

            print("buffers: {} bytes".format(len(buffer)))

            # integer count
            indexes = ' '.join(str(n).zfill(2) for n in range(len(buffer)))
            print(indexes)

            # convert to a readable hex tree
            hex_buffer = hexlify(buffer).decode('ascii')
            # split pair of digits with white spaces
            # we can do it by slicing out consecutive pairs
            hex_pairs = ' '.join(hex_buffer[i:i + 2]
                                 for i in range(0, len(hex_buffer), 2))
            print(hex_pairs)

            # memoryview object
            mem = memoryview(buffer)
            print(mem)

            # Size of the vertex structure
            VERTEX_SIZE = 18
            # Strides between successful vertix structure, 2 byte padding between the
            # sctructures
            VERTEX_STRIDE = VERTEX_SIZE + 2

            # suspend the program and drop us to the REPL session
            # code.interact(local=locals())

            # use stuct unpack function to convert raw byte sequence into more friendly
            # types. @fffHHH - format string here
            # @ - specify native byte order, native size and alignment are to be used.
            # fff - tells struct to expect a single precision c float
            # HHH - tells struct to expect an ansigned short int, which is 16-bit type
            # xx - pad byte, tells struct to expect aligned longs of bytes on 2-byte
            # boundaries
            # For more details of parameters and datatyped please see the struct
            # library documentation

            # items = struct.unpack_from('@fffHHH', buffer)

            # specify in more convenient way,numner 3 uses to reduce data series
            # x, y, z, red, green, blue = struct.unpack_from('@3f3H', buffer)

            # vertices = []
            # # Successfully read out structures from C into Python
            # for fields in struct.iter_unpack('@3f3Hxx', buffer):
            #     vertex = make_colored_vertex(*fields)
            #     vertices.append(vertex)

            # generator expressions which yield successive memory views
            # into whole vertex structure
            vertex_mems = (mem[i:i + VERTEX_SIZE]
                           for i in range(0, len(mem), VERTEX_STRIDE))
            # build the list of vertices
            vertices = [make_colored_vertex(vertex_mem)
                        for vertex_mem in vertex_mems]

            # now our vector and color objects are backed by the binary datai
            # we loaded from the file with much reduced copying
            pp(vertices)

            # empty register in order to close exported pointers
            del vertices
            del mem


if __name__ == '__main__':
    main()
