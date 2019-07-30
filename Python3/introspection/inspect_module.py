import inspect
import sorted_set


if __name__ == "__main__":
    print(inspect.ismodule(sorted_set))
    # retrieves members as a list of name value pairs
    print(inspect.getmembers(sorted_set))
    # contains 16 predicates for identifying different object types from
    # isabstract
    print(dir(inspect))
    # Get all classes of the sorted_set module by isclass predicate
    print(inspect.getmembers(sorted_set, inspect.isclass))

    from sorted_set import chain
    print(list(chain([1, 2, 3], [4, 5, 6])))

    # Get all functions of the SortedSet class by isfunctions predicate
    print(inspect.getmembers(sorted_set.SortedSet, inspect.isfunction))

    # Retrieve the signature if dunder-init on our SortedSet class
    init_sig = inspect.signature(sorted_set.SortedSet.__init__)
    print(init_sig)
    print(init_sig.parameters)
    print(repr(init_sig.parameters['items'].default))
    print(str(init_sig))
    # print(inspect.signature(abs))  # will receive an error because abs is
    # built-in function, which is implemented in C don't provide sufficient
    # metadata
