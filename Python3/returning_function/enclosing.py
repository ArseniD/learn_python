def enclosing():
    def local_func():
        print('local func')
    return local_func


if __name__ == "__main__":
    lf = enclosing()
    print(lf())
