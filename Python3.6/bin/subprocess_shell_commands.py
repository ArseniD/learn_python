#!/usr/bin/env python3.6

import subprocess

proc = subprocess.run(["ls", "-l"])
proc

proc = subprocess.run(
    ['ls', '-l'],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
)

print(proc.stdout)
print(proc.stdout.decode())

new_proc = subprocess.run(['cat', 'fake.txt'])
new_proc

new_proc = subprocess.run(['cat', 'fake.txt'], check=True)
new_proc
