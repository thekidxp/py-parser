#!/usr/bin/python3
import sys
import json
import xml.etree.ElementTree as Et

file_type = sys.argv[1]
if file_type.casefold() == '-x'.casefold():
    find_string = sys.argv[2]
    print(Et.parse(sys.stdin).find(f'*/{find_string}').text)
else:
    find_string = sys.argv[1]
    print(json.load(sys.stdin)[find_string])
