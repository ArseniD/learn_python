#!/usr/bin/env python3.6

xmen_file = open('xmen_base.txt', 'r')
print(xmen_file)
print(xmen_file.read())

xmen_file.seek(6)
print(xmen_file.read())

xmen_file = open('xmen_base.txt', 'r')
for line in xmen_file:
    print(line, end="")
xmen_file.close()

xmen_base = open('xmen_base.txt')
new_xmen = open('new_xmen.txt', 'w')
new_xmen.write(xmen_base.read())

new_xmen.close()
new_xmen = open(new_xmen.name, 'r+')
new_xmen.read()
new_xmen.seek(0)
new_xmen.write("Beast\n")
new_xmen.write("Phoenix\n")
new_xmen.seek(0)
print(new_xmen.read())

xmen_base.close()
with open('xmen_base.txt', 'a') as f:
    f.write("Professor Xavier\n")
