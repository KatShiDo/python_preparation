import re

def parse_string(data):
    result = {}
    matches = re.findall(r'def\s+list\(\s*([^\)]+)\s*\)\s*=\:\s*([^\.\s]+)', data)
    for match in matches:
        values = [int(x) for x in match[0].split()]
        result[match[1]] = values
    return result