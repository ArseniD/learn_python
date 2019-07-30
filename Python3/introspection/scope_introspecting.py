if __name__ == "__main__":
    print(globals())  # represents the global namespace
    a = 42
    print(globals())
    globals()['tai'] = 4.3213  # add variable to the global namespace
    print(tai)
    print(tai / 2)

    print(locals())  # locals will return the same dictinary as globals

    def report_scope(arg):
        from pprint import pprint as pp
        x = 496
        pp(locals(), width=10)

    report_scope(42)

#  Check out locals variables
    name = "Arseni Dudko"
    age = 28
    country = "Minsk"

    print("{name} is {age} years old and is from {country}".format(**locals()))
