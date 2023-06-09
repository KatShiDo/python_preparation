import re

def parse_string(input_string):
    result = []
    matches = re.findall(r'<data>\s*(-?\d+)\s+=:\s+@"(.+?)";', input_string)
    for match in matches:
        result.append((match[1], int(match[0])))
    return result