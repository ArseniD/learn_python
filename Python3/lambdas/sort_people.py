people = ['Anton B', 'Victor A', 'Eugene Z', 'Jack C', 'Marry X', 'Kenny Y']


if __name__ == "__main__":
    result = sorted(people, key=lambda name: name.split()[-1])
    print(result)

    last_name = lambda name: name.split()[-1]
    print(last_name('Anton A'))

    def first_name(name):
        return name.split()[0]

    print(last_name('Anton B'))
