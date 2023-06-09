import re

def parse_string(data):
    result = []
    matches = re.findall(r'global\s+q\(([^\)]+)\)\s*<=\s*([^\s:>]+)', data)
    for match in matches:
        result.append((match[0], match[1]))
    return result