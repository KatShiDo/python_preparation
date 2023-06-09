import re

def parse_string(input_string):
    result = []
    matches = re.findall(r'make\s+(\w+)\s+<\|\s+list\((.+?)\)', input_string)
    for match in matches:
        numbers = [int(n) for n in match[1].split()]
        result.append((match[0], numbers))
    return result