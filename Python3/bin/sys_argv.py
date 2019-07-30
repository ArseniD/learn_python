#!/usr/bin/env python3.6

"""
Check it our by running following commands from cosole:
    ./sys_argv testing
    ./sys_argv testing testing12 'another argument'
"""

import sys

print(f"Positional arguments: {sys.argv[1:]}")
print(f"First argument: {sys.argv[1]}")
