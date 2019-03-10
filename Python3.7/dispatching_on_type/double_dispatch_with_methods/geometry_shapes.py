from fractions import Fraction
from functools import singledispatch
from math import sqrt


class Shape:

    def __init__(self, solid):
        self.solid = solid


class Circle(Shape):

    def __init__(self, center, radius, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.center = center
        self.radius = radius

    def intersects(self, shape):
        # Delegate to the generic function, swapping arguments
        return intersects_with_circle(shape, self)


class Parallelogram(Shape):

    def __init__(self, pa, pb, pc, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pa = pa
        self.pb = pb
        self.pc = pc

    def intersects(self, shape):
        # Delegate to the generic function, swapping arguments
        return intersects_with_circle(shape, self)


class Triangle(Shape):

    def __init__(self, pa, pb, pc, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pa = pa
        self.pb = pb
        self.pc = pc

    def intersects(self, shape):
        # Delegate to the generic function, swapping arguments
        return intersects_with_circle(shape, self)


@singledispatch
def draw(shape):
    """
    Implement generic draw function
    The object returned by the singledispatch decorator is bound
    to the name "draw"

    By default raise the type error
    this is the version we will recall when we haven't provided an overload
    for a specific type of shape - Circle, Parallelogram or Triangle
    """
    raise TypeError("Don't know how to draw {!r}".format(shape))


@draw.register(Circle)
def _(shape):
    """
    the wrapper returned by the decorator is bound to the name draw
    The draw wrapper has an attribute called register,
    which is also a decorator,
    which can be used to provide additional version of the orignal function,
    which work on different types. This is function overloading.
    Since overload will be associated with the name of the original function,
    draw, it doesn't matter what we call the the overloads themselves, so by
    convention we call them underscore '_'.
    Whatever name we use for this function will be ignored.
    """
    print("\u25CF" if shape.solid else "\u25A1")


@draw.register(Parallelogram)
def _(shape):
    print("\u25B0" if shape.solid else "\u25B1")


@draw.register(Triangle)
def _(shape):
    print("\u25B2" if shape.solid else "\u25B3")


@singledispatch
def intersects_with_circle(shape, circle):  # by default raise the type error
    raise TypeError("Don't know how to compute intersection of {!r} with {!r}"
                    .format(circle, shape))


@intersects_with_circle.register(Circle)
def _(shape, circle):
    return circle_intersects_circle(circle, shape)


@intersects_with_circle.register(Parallelogram)
def _(shape, circle):
    return circle_intersects_parallelogram(circle, shape)


@intersects_with_circle.register(Triangle)
def _(shape, circle):
    return circle_intersects_triangle(circle, shape)


def circle_intersects_circle(circle, shape):
    """
    Define whether cicrle intersects circle or not.

    args:
        circle - contains a coordinates of first circle center and his radius
        shape - contains a coordinates of second circle center and his radius

    prints: position of a circles
    """

    # Specify the center of circle 1 and 2 and radius R1 and R2
    X1, Y1 = circle.center[0], circle.center[1]
    X2, Y2 = shape.center[0], shape.center[1]
    R1 = circle.radius
    R2 = shape.radius

    # Find the distance between circles cente
    d = sqrt((X1 - X2) ** 2 + (Y1 - Y2) ** 2)

    # Find sum of raius and their difference
    Rsum = R1 + R2
    Rdif = R1 - R2

    if d > Rsum:
        print("Circles do not intersect")
    elif d < Rsum and d > abs(Rdif):
        print("Circles do intersect in two points")
    elif d == Rsum:
        print("Circles touch")
    elif d == 0 and R1 != R2:
        print("Circles are concentric")
    else:
        print("Circles coincide and have common tangent")


def circle_intersects_parallelogram(circle, shape):
    """
    Define whether cicrle intersects parallelogram/quadrangle/line or not.

    args:
        circle - contains coordinates of a circle center "O" and his radius "R"
        shape - contains coordinates of points A, B and C

    prints: the shape that do intersect a circle or not
    """
    # Define points ABC in more convenient way
    A = (shape.pa[0], shape.pa[1])
    B = (shape.pb[0], shape.pb[1])
    C = (shape.pc[0], shape.pc[1])
    R = circle.radius
    Ox, Oy = (circle.center[0], circle.center[1])

    # Find 3 possible coordinates of D point
    D1 = (A[0] - B[0] + C[0], A[1] - B[1] + C[1])
    D2 = (B[0] - C[0] + A[0], B[1] - C[1] + A[1])
    D3 = (C[0] - A[0] + B[0], C[1] - A[1] + B[1])

    # Use slope formula to prove that ABCD is a parallelogram
    ABx = (B[1] - A[1])
    ABy = (B[0] - A[0])
    CDx = (D1[1] - C[1])
    CDy = (D1[0] - C[0])

    # Check whether points A, B and C form a line or ABCD is a parallelogram
    is_line = is_collinear_points(A, B, C)
    is_parallelogram = is_pair_equal(ABx, ABy, CDx, CDy) and not is_line

    # Find the distance between all points and circle center
    points = [A, B, C, D1, D2, D3]
    dists = points_distance(Ox, Oy, points)

    # Find all intersects points with a circle
    intersects_points = intersect_points(dists, R)

    # Find and print what shape do instersect Circle or not
    while intersects_points:
        if is_parallelogram:
            print("Parallelogram intersects Circle")
            break
        if is_line:
            print("Line intersects Circle")
            break
        # if not is_parallelogram and not is_line:
        print("Quadrangle intersects Circle")
        break
    else:  # nonbreak
        if is_parallelogram:
            print("Parallelogram do not intersect Circle")
        if is_line:
            print("Line do not intersect Circle")
        if not is_parallelogram and not is_line:
            print("Quadrangle do not intersect Circle")


def circle_intersects_triangle(circle, shape):
    """
    Find the intersecting points between cicrle and triangle if it exists.

    args:
        circle - contains coordinates of circle center "O" and his radius "R"
        shape - contains coordinates of points A, B and C

    prints: triangle/line intersects circle or not based on conditions
    """
    # Specify points in more convenient way
    A = (shape.pa[0], shape.pa[1])
    B = (shape.pb[0], shape.pb[1])
    C = (shape.pc[0], shape.pc[1])
    R = circle.radius
    O = (circle.center[0], circle.center[1])

    # Check whether or not sides intersect circle
    AB = circle_segment_intersect(A, B, O, R)
    BC = circle_segment_intersect(B, C, O, R)
    AC = circle_segment_intersect(A, C, O, R)

    # Check whether or not points A, B and C lie on the same line
    is_line = is_collinear_points(A, B, C)

    # Form a dict with True or False sides
    sides = {'AB': AB, 'BC': BC, 'AC': AC}
    # Find all True sides from the dict that intersect circle
    intersects_sides = dict(filter(lambda x: x[1], sides.items()))
    # Form pretty output
    output = '\n'.join([f'{k}: {v}' for k, v in intersects_sides.items()])

    # Find and print all points with their sides that intersect circle
    while intersects_sides:
        if not is_line:
            print(f'Triangle intersects circle in points:\n{output}')
            break
        print(f'Line intersects circle in points:\n{output}')
        break
    else:  # nonbreak
        if is_line:
            print("Line do not intersect circle")
        if not is_line:
            print("Triangle do not intersect circle")


def points_distance(cent_x, cent_y, points):
    """
    Find the distance between all points and circle center

    args:
        cent_x - circle center x coordinate
        cent_y - circle center y coordinate
        points - list of the points [A, B, C, D, ..]

    returns: list of the distance between each point and circle center
    """
    dists = [sqrt((x - cent_x) ** 2 + (y - cent_y) ** 2) for x, y in points]
    return dists


def intersect_points(distance, R):
    """
    Find all intersecting points with a circle

    args:
        distance - a list of distance between each point and circle center
        R - circle radius

    returns: a list with intersecting points
    """
    points = list(filter(lambda d: d < R, distance))
    return points


def is_collinear_points(A, B, C):
    """
    Check that points are collinear.
    The difference of dot product should be equal to 0

    args:
        A - coordinate of point A
        B - coordinate of point B
        C - coordinate of point C

    returns: True if Diff is equal to 0 otherwise False
    """
    Diff = (A[0] * B[1] + B[0] * C[1] + C[0] * A[1]) - \
        (B[0] * A[1] + C[0] * B[1] + A[0] * C[1])
    return True if Diff == 0 else False


def is_pair_equal(AB_x, AB_y, CD_x, CD_y):
    """
    Check weither a points form paralleogram or not

    args:
        AB_x, AB_y, CD_x, CD_y - a coordinates of quadrangle

    returns: True if opposite sides are pairwise parallel else False
    """
    num_1 = AB_x
    den_1 = AB_y
    num_2 = CD_x
    den_2 = CD_y

    AB = Fraction(num_1, den_1) if den_1 != 0 else 0
    CD = Fraction(num_2, den_2) if den_2 != 0 else 0

    return abs(AB) == abs(CD) != 0


def is_point_on_segment(A, B, P):
    """
    Check if a point belongs on a line segment

    args:
        A - coordinate of known point A
        B - coordinate of known point B
        P - coordinate of a point we want to check

    return: True if point P belongs to segment AB else False
    """

    # Specify points in more convenient way
    X1, Y1 = (A[0], A[1])
    X2, Y2 = (B[0], B[1])
    Xp, Yp = (P[0], P[1])

    # Based on segmet equation: pOA+(1-p)OB=P,
    # express 'p' from the first euation and paste it to the second
    # px1+(1-p)x2=x
    # py1+(1-p)y2=y
    num = Xp - X2
    den = X1 - X2
    p = num / den if den != 0 else 0

    # Check that left and right expressions are equal and p in the range [0..1]
    # Here I used "round" in order to avoid the error of number measurements
    return round(p * Y1 + (1 - p) * Y2, 15) == round(Yp, 15) and 0 <= p <= 1


def circle_segment_intersect(A, B, O, R):
    """
    Check weither a segment intersects/touches circle or not

    args:
        A - coordinates of the begining of a segment
        B - coordinates of the end of a segment
        O - coordinates of a circle center
        R - a circle radius

    returns: coordinates of points where circle intersects with a segment
    or False if they does not exist
    """
    # Specify points in more convenient way
    X1, Y1 = (A[0], A[1])
    X2, Y2 = (B[0], B[1])
    Ox, Oy = (O[0], O[1])

    # Find a coordinates of direction vector AB, from start to end
    Dx, Dy = (X2 - X1, Y2 - Y1)

    # a, b and c (ax*2+bx+c=0) are the coefficients that we received by solving
    # the system of parametric equation of the line and circle equation:
    # X(t) = X1 + (X2 - X1) * t
    # Y(t) = Y1 + (Y2 - Y1) * t
    # (X - Ox)**2 + (Y - Oy)**2 = radius**2
    a = Dx**2 + Dy**2
    b = 2 * (Dx * (X1 - Ox) + Dy * (Y1 - Oy))
    c = (X1 - Ox)**2 + (Y1 - Oy)**2 - R**2
    # Find the discriminant "d"
    d = b**2 - 4 * a * c

    if d > 0 and A != B:
        t1 = (-b + sqrt(d)) / (2 * a)
        t2 = (-b - sqrt(d)) / (2 * a)
        # Substitute the value of t into the formula:X(t) = X1 + (X2 - X1) * t
        # and find the points of line that intersect circle
        p1 = (X1 + t1 * Dx, Y1 + t1 * Dy)
        p2 = (X1 + t2 * Dx, Y1 + t2 * Dy)
        # Check whether p1 and p2 belongs to the segment of AB and return the
        # value if it does
        if is_point_on_segment(A, B, p1) and is_point_on_segment(A, B, p2):
            return p1, p2
        if is_point_on_segment(A, B, p1):
            return p1
        if is_point_on_segment(A, B, p2):
            return p2
        else:
            return False
    if d == 0 and A != B:
        t = -b / (2 * a)
        p = (X1 + t * Dx, Y1 + t * Dy)
        return p if is_point_on_segment(A, B, p) else False
    if d < 0 or A == B:
        return False


def main():

    circle = Circle(center=(-3, 4), radius=4, solid=False)

    shapes = [
        Circle(center=(1, 0), radius=2, solid=True),
        Circle(center=(-3, 4), radius=9, solid=True),
        Circle(center=(-3, 4), radius=4, solid=True),
        Circle(center=(0, 0), radius=1, solid=True),

        Parallelogram(pa=(2, -1), pb=(-1, 1), pc=(1, 3), solid=True),
        Parallelogram(pa=(1, 3), pb=(2, 3), pc=(3, 3), solid=False),
        Parallelogram(pa=(1, 3), pb=(1, 4), pc=(5, 3), solid=True),
        Parallelogram(pa=(9, -3), pb=(8, -2), pc=(7, -2), solid=False),
        Parallelogram(pa=(3, -3), pb=(4, -3), pc=(5, -3), solid=False),
        Parallelogram(pa=(4, 3), pb=(4, 4), pc=(5, 3), solid=False),

        Triangle(pa=(-3, 3), pb=(-4, 6), pc=(-3, 3), solid=False),
        Triangle(pa=(1, 4), pb=(1, 4), pc=(-3, 3), solid=True),
        Triangle(pa=(-3, 4), pb=(-4, 6), pc=(-3, 3), solid=False),
        Triangle(pa=(0, 0), pb=(-4, 6), pc=(-3, 3), solid=True),
        Triangle(pa=(1, 4), pb=(-4, 6), pc=(-3, 3), solid=True),
        Triangle(pa=(2, 3), pb=(-8, 8), pc=(-3, 8), solid=True),
        Triangle(pa=(2, 3), pb=(-8, -8), pc=(-3, 8), solid=True),
    ]

    for shape in shapes:
        draw(shape)
        circle.intersects(shape)


if __name__ == "__main__":
    main()
