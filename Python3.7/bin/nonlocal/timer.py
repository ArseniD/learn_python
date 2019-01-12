import time


def make_timer():
    last_called = None

    def elapsed():
        nonlocal last_called
        now = time.time()
        if last_called is None:
            last_called = now
            return None
        result = now - last_called
        last_called = now
        return result

    return elapsed


if __name__ == "__main__":
    t_1 = make_timer()  # one object
    t_2 = make_timer()  # another object

    print(t_1())
    print("{:f}".format(t_1()))
    print("{:f}".format(t_1()))
    print("{:f}".format(t_1()))

    print(t_2())
    print("{:f}".format(t_2()))
    print("{:f}".format(t_2()))
    print("{:f}".format(t_2()))
