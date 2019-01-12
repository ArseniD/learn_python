import itertools


if __name__ == "__main__":
    result = map(ord, 'The quick brown fox')
    print(list(result))

    for x in map(ord, 'The quick brown fox'):
        print(x)


    size = ['small', 'medium', 'large']
    colors = ['lavenger', 'teal', 'burnt orange']
    animals = ['koala', 'platypus', 'sloth']

    def combine(size, color, animal):
        return '{} {} {}'.format(size, color, animal)

    print(list(map(combine, size, colors, animals)))


    def combine_2(quantity, size, color, animal):
        return '{} x {} {} {}'.format(quantity, size, color, animal)

    print(list(map(combine_2, itertools.count(), size, colors, animals)))


#  comprehension vs map()
    print([str(i) for i in range(5)])
    print(list(map(str, range(5))))

    i = (str(i) for i in range(5))
    print(list(i))

    i = map(str, range(5))
    print(list(i))
