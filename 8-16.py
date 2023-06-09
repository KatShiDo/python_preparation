import re

def parse_string(input_string):
    result = {}
    matches = re.findall(r'global\s+#(-?\d+)\s*\|>\s*q\((.+?)\)', input_string)
    for match in matches:
        result[match[1]] = int(match[0])
    return result