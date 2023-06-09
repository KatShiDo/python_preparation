import re

def parse_string(input_string):
    result = {}
    matches = re.findall(r'equ\s+(\w+)\s+q\((.+?)\)', input_string)
    for match in matches:
        result[match[0]] = match[1]
    return result