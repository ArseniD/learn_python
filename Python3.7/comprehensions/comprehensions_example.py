if __name__ == "__main__":
    l = [i * 2 for i in range(10)]
    print(type(l))
    print(dir(l))
    print(l)
    l.append(42)
    print(l)

    d = {i: i * 2 for i in range(10)}
    print(type(d))
    print(d)

    s = {i for i in range(10)}
    print(type(s))
    print(s)

    g = (i for i in range(10))
    print(type(g))
    print(g)


    point = [(x, y) for x in range(5) for y in range(3)]
    print(point)

    #  The same as above
    points_2 = []
    for x in range(5):
        for y in range(3):
            points_2.append((x, y))

    print(points_2)


    values = [x / (x - y)
              for x in range(100)
              if x > 50
              for y in range(100)
              if x - y != 0]

    print(values)

    #  The same as above
    values_2 = []
    for x in range(100):
        if x > 50:
            for y in range(100):
                if x - y != 0:
                    values_2.append(x / (x - y))

    print(values_2)


    result = [(x, y) for x in range(10) for y in range(x)]
    print(result)

    #  The same as above
    result_2 = []
    for x in range(10):
        for y in range(x):
            result_2.append((x, y))

    print(result_2)
