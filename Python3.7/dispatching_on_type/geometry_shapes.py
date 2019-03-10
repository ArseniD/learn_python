from functools import singledispatch


class Shape:

    def __init__(self, solid):
        self.solid = solid


class Circle(Shape):

    def __init__(self, center, radius, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.center = center
        self.radius = radius


class Parallelogram(Shape):

    def __init__(self, pa, pb, pc, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pa = pa
        self.pb = pb
        self.pc = pc


class Triangle(Shape):

    def __init__(self, pa, pb, pc, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pa = pa
        self.pb = pb
        self.pc = pc


@singledispatch
# implement generic draw function
# The object returned by the singledispatch decorator is bound to the name
# "draw"
def draw(shape):  # by default raise the type error
    # this is the version we will recall when we haven't provided an overload
    # for a specific type of shape - Circle, Parallelogram or Triangle
    raise TypeError("Don't know how to draw {!r}".format(shape))


@draw.register(Circle)
# the wrapper returned by the decorator is bound to the name draw
# The draw wrapper has an attribute called register, which is also a decorator,
# which can be used to provide additional version of the orignal function,
# which work on different types. This is function overloading.
# Since overload will be associated with the name of the original function,
# draw, it doesn't matter what we call the the overloads themselves, so by
# convention we call them underscore '_'. Whatever name we use will be ignored.
def _(shape):
    print("\u25CF" if shape.solid else "\u25A1")


@draw.register(Parallelogram)
def _(shape):
    print("\u25B0" if shape.solid else "\u25B1")


@draw.register(Triangle)
def _(shape):
    print("\u25B2" if shape.solid else "\25B3")


# def draw(shape):
#     if isinstance(shape, Circle):
#         draw_circle(shape)
#     elif isinstance(shape, Parallelogram):
#         draw_parallelogram(shape)
#     elif isinstance(shape, Triangle):
#         draw_triangle(shape)
#     else:
#         raise TypeError("Can't draw shape {!r}".format(shape))


# def draw(shape):
#     drawers = {
#         Circle: draw_circle,
#         Parallelogram: draw_parallelogram,
#         Triangle: draw_triangle,
#     }

#     try:
#         drawer = drawers[type(shape)]  # better to use single dispatching
#     except KeyError as e:
#         raise TypeError("Can't draw shape") from e
#     else:
#         drawer(shape)

# Now drawing is dependent on shaped, but not shapes on drawing
# Our main function just call the global scope generic draw function for each
# item, and the single dispatch machinery will select the most specific
# overload if one exists or fall back to the default implementation. We could
# add other capabilities to shape in a similiar way by defining other generic
# funcions, which behave polymorphically with respect to the shape types.
def main():
    shapes = [Circle(center=(0, 0), radius=5, solid=False),
              Parallelogram(pa=(0, 0), pb=(2, 0), pc=(1, 1), solid=False),
              Triangle(pa=(0, 0), pb=(1, 2), pc=(2, 0), solid=True)]

    for shape in shapes:
        draw(shape)


if __name__ == "__main__":
    main()
