def is_comment(item):
    return isinstance(item, str) and item.startswith('#')


def execute(program):
    """Execute  a stack program.

    Args:
        program: Any stack-like containing where each item in the stack
        is a callable operators or non-callable operands. The top-most items
        on the stack may be strings beginning with '#' for the purposes of
        documentation. Stack-like means support for:

            item = stack.pop()  # Remove and return the top item
            stack.append(item)  # Push an item to the top
            if stack:           # False in a boolean context when empty
    """
    # Find the start of the 'program' by skipping any iten which is a comment
    while program:
        item = program.pop()
        if not is_comment(item):
            program.append(item)
            break
    else:  # nonbreak
        print("Empty program!")
        return

    # Evaluate the program
    pending = []  # a collection of numbers
    while program:
        item = program.pop()
        if callable(item):
            try:
                # perform a callable operator action on numbers colletion
                # in the 'pending' list
                result = item(*pending)
            except Exception as e:
                print("Error: ", e)
                break
            # write a result of calculation
            program.append(result)
            pending.clear()
        else:
            pending.append(item)
    else:
        print("Program succcessful")
        print("Result: ", pending)

    print("Finished")


if __name__ == "__main__":
    import operator

    # the top of the stack is the end of the list and that is why we're using
    # revered list while removing the last indexing with 'program.pop()' method
    program = list(reversed((
        "# A short stack program to add",
        "# and multiply some constants",
        5,
        2,
        operator.add,
        3,
        operator.mul)))

    execute(program)
