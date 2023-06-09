import re

def parse_string(input_string):
    result = []
    matches = re.findall(r'data\s*#\s*\((.+?)\)\s*\|>\s*\'(.+?)\'', input_string)
    for match in matches:
        data = [d.strip().strip('\'') for d in match[0].split(',')]
        result.append((match[1], data))
    return result