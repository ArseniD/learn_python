#!/usr/bin/env python3.6

import subprocess
import os
from sys import exit
from argparse import ArgumentParser

parser = ArgumentParser(description='kill the running process listening on a given port')
parser.add_argument('port', type=int, help='the number of portt kill')

port = parser.parse_args().port

proc = subprocess.run(
    ['lsof', '-n', f'-i4TCP:{port}'],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE)

try:
    pid = int((proc.stdout.decode().split())[-9])

    if pid:
        os.kill(pid, 9)
        print(f"Process on port {port} has been terminated")
except IndexError as err:
    print(f"There is no process listerning on port {port}")
    exit(1)
