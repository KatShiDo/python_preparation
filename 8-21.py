import re

def parse_string(data):
    result = []
    matches = re.findall(r'def\s+([^\s|>]+)\s*\|>\s*q\(([^\)]+)\)', data)
    for match in matches:
        result.append((match[1], match[0]))
    return result