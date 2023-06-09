import re

def parse_string(input_string):
    result = []
    matches = re.findall(r'global\s+(\w+)\s+to\s+\'(.+?)\'', input_string)
    for match in matches:
        result.append((match[1], match[0]))
    return result