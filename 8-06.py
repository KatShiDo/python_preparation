import re

def parse_string(input_string):
    result = []
    matches = re.findall(r'make\s+q\((.+?)\)\s+#(-?\d+)', input_string)
    for match in matches:
        result.append((match[0], int(match[1])))
    return result