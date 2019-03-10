# items = [2, 24, 22, 4]
# divisor = 12
# # divisor = 13

# for item in items:
#     if item % divisor == 0:
#         found = item
#         break
# else:  # nonbreak
#     items.append(divisor)
#     found = divisor


def has_divisible(items, divisor):
    for item in items:
        if item % divisor == 0:
            return item
    items.append(divisor)
    return divisor


items = [1, 23, 3]
divisor = 12

dividend = has_divisible(items, divisor)


print("{items} contains {dividend} which is a multiple of {divisor}"
    .format(**locals()))
