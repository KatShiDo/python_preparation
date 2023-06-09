import re

def parse_string(input_string):
    result = {}
    matches = re.findall(r'global\s+q\((.+?)\)\s*=\s*(.+?)\.', input_string)
    for match in matches:
        result[match[0]] = match[1].strip()
    return result