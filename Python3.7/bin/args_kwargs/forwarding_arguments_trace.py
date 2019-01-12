def trace(f, *args, **kwargs):
    print("args =", args)
    print("kwargs =", kwargs)
    result = f(*args, **kwargs)  # forwarding arguments to the int function
    return result


if __name__ == "__main__":
    print(int("ff", base=16))

    print(trace(int, "ff", base=16))
