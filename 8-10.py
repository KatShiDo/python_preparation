import re

def parse_string(input_string):
    result = []
    matches = re.findall(r'val\s+(\w+)\s+=\s+#\(\s*(.+?)\s*\)', input_string)
    for match in matches:
        data = [d.strip().strip('\'') for d in match[1].split(';')]
        result.append((match[0], data))
    return result