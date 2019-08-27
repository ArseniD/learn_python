#!/home/juzo/Documents/Linuxacademy/Python3.6/venvs/experiment/bin/python

import os
import requests
import sys

from argparse import ArgumentParser

parser = ArgumentParser(description="Get and store the web page content in 'JSON' or 'HTML' formats")
parser.add_argument('url', help='web page url')
parser.add_argument('filename', help='the filename to store the content under')
parser.add_argument('--format', '-f',
                    default='HTML',
                    choices=['html', 'json'],
                    help='the content type of the URL, default is "HTML"')

args = parser.parse_args()

res = requests.get(args.url)

if res.status_code >= 400:
    print(f"Error code received: {res.status_code}")
    sys.exit(1)

if args.format == 'JSON':
    try:
        content = json.dump(res.json())
    except ValueError:
        print("Error: Content is not JSON")
        sys.exit(1)
else:
    content = res.text

with open(args.filename, 'w', encoding='UTF-8') as f:
    f.write(content)
    print(f"Content written to '{args.filename}'")
