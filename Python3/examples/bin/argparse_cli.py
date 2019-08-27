#!/usr/bin/env python3.6

import argparse

# build the parser
parser = argparse.ArgumentParser()
parser.add_argument('filename', help='the file to read')
parser.add_argument('--limit', '-l', type=int, help='the number of lines to read')
parser.add_argument('--version', '-v', action='version', version='%(prog)s 1.0')

# parse the arguments
args = parser.parse_args()

# read the file, reverse the contens and print
with open(args.filename) as f:
    lines = f.readlines()
    lines.reverse()

    if args.limit:
        lines = lines[:args.limit]

    for line in lines:
        print(line.strip()[::-1])
