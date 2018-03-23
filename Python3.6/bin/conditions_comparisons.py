#!/usr/bin/env python3.6

if True:
    print("Was True")

if False:
    print("Was True")

if False:
    print("Was True")
else:
    print("Was False")


name = "Kevin"
if len(name) >= 6:
    print("name is long")
elif len(name) == 5:
    print("name is 5 characters")
elif len(name) >= 4:
    print("name is 4 or more")
else:
    print("name is short")
