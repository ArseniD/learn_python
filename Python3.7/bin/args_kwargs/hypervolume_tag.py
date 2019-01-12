def hypervolume_test(*args):
    print(args)
    print(type(args))


def hypervolume_1(*lengths):
    i = iter(lengths)
    v = next(i)
    for lenght in i:
        v *= lenght
    return v


def hypervolume_2(length, *lengths):
    v = length
    for item in lengths:
        v *= item
    return v


def tag_1(name, **kwargs):
    print(name)
    print(kwargs)
    print(type(kwargs))


def tag_2(name, **attributes):
    result = '<' + name
    for key, value in attributes.items():
        result += ' {k}="{v}"'.format(k=key, v=str(value))
    result += '>'
    return result


def print_args(arg1, arg2, *args):
    print(arg1)
    print(arg2)
    print(args)


def print_args_2(arg1, arg2, *args, kwarg1, kwarg2):
    print(arg1)
    print(arg2)
    print(args)
    print(kwarg1)
    print(kwarg2)


def print_args_3(arg1, arg2, *args, kwarg1, kwarg2, **kwargs):
    print(arg1)
    print(arg2)
    print(args)
    print(kwarg1)
    print(kwarg2)
    print(kwargs)


def color(red, green, blue, **kwargs):
    print("r =", red)
    print("g =", green)
    print("b =", blue)
    print(kwargs)


if __name__ == "__main__":
    print(hypervolume_test(3, 4))
    print(hypervolume_test(3, 4, 5))

    print(hypervolume_1(2, 4))
    print(hypervolume_1(2, 4, 6))
    print(hypervolume_1(2, 4, 6, 8))
    print(hypervolume_1(1))

    print(hypervolume_2(3, 5, 7, 9))
    print(hypervolume_2(3, 5, 7))
    print(hypervolume_2(3, 5))
    print(hypervolume_2(3))

    print(tag_1('img', src="monet.jpg", alt="Sunrise by Claude Monet", border=1))
    print(tag_2('img', src="monet.jpg", alt="Sunrise by Claude Monet", border=1))

    print(print_args(1, 2, 3, 4, 5))
    t = (11, 12, 13, 14)
    print(print_args(*t))

    print(print_args_2(1, 2, 3, 4, 5, kwarg1=6, kwarg2=7))
    print(print_args_3(1, 2, 3, 4, 5, kwarg1=6, kwarg2=7, kwarg3=8, kwarg4=9))

    k = {'red':21, 'green':68, 'blue':120, 'alpha':52}
    print(color(**k))
