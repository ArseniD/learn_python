message = 'global'

def enclosing():
    message = 'enclosing'

    def local():
        global message
        message = 'local'

    print('enclosing message:', message)
    local()
    print('enclosing message:', message)


if __name__ == "__main__":
    print('global message:', message)
    print(enclosing())
    print('global message:', message)
