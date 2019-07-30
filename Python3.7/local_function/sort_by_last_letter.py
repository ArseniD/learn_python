store = []

def sort_by_last_letter(string):

    def last_letter(s):  # definded each time sort_by_last_letter is called
        return s[-1]
    store.append(last_letter)
    print(last_letter)  # should show different objects
    return sorted(string, key=last_letter)


g = 'global'

def outer(p='param'):
    l = 'local'

    def inner():
        print(g, p, l)
    inner()


if __name__ == "__main__":
    print(sort_by_last_letter(['xxxZ', 'xxxY', 'xxxX', 'xxxA', 'xxxB']))
    print(sort_by_last_letter(['xxxZ', 'xxxY', 'xxxX', 'xxxA', 'xxxB']))
    print(sort_by_last_letter(['xxxZ', 'xxxY', 'xxxX', 'xxxA', 'xxxB']))

    print(outer())
