import re

def parse_string(input_string):
    result = []
    matches = re.findall(r'glob\s+list\((.+?)\)\s*\|>\s*(.+?);', input_string)
    for match in matches:
        data = [d.strip() for d in match[0].split(',')]
        result.append((match[1], data))
    return result