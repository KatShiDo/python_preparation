import re

def parse_string(input_string):
    result = []
    matches = re.findall(r'opt\s+q\((.+?)\)\s+\|>\s+(.+?)\s+end', input_string)
    for match in matches:
        result.append((match[1], match[0]))
    return result