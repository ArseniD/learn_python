# Conditional statement
# def sequence_class(immutable):
#     if immutable:
#         cls = tuple
#     else:
#         cls = list
#     return cls

# Conditional exspression
def sequence_class(immutable):
    return tuple if immutable else list


if __name__ == "__main__":
    seq_1 = sequence_class(immutable=True)
    inst_1 = seq_1("Arseni")
    print(inst_1)
    print(type(inst_1))

    seq_2 = sequence_class(immutable=False)
    inst_2 = seq_2("Arseni")
    print(inst_2)
    print(type(inst_2))
