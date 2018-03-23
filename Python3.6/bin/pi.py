#!/usr/bin/env python3.6

from os import getenv
from math import pi

digit = int(getenv("DIGITS") or 10)
print("%.*f" % (digit, pi))
