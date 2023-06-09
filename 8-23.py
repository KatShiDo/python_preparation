import re

def parse_string(data):
    result = []
    matches = re.findall(r'var\s+([^\s<]+)\s*<-\s*\{\s*([^\}]+)\s*\}', data)
    for match in matches:
        values = [x.strip() for x in match[1].split(';')]
        result.append((match[0], values))
    return result