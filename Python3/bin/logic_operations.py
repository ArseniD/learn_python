#!/usr/bin/env python3.6

name = ""
not name

if not name:
    print("No name given")

first = ""
last = "Thompson"
if first or last:
    print("The user has a first or last name")

first = ""
last = ""
if first or last:
    print("The user has a first or last name")

last = ""
last_name = last or "Doe"
print(last_name)

print(0 or 1 or 2)


first = "Keith"
last = ""
if first and last:
    print(f"Full name: {first} {last}")
elif first:
    print(f"First name: {first}")
elif last:
    print(f"Last name: {last}")


first = "Keith"
last = "Thompson"
if first and last:
    print(f"Full name: {first} {last}")
elif first:
    print(f"First name: {first}")
elif last:
    print(f"Last name: {last}")

print(0 and 1)
print(1 and 2)

print((1 == 1) and print("Something"))
print((1 == 2) and print("Something"))
