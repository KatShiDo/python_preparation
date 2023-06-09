import re

def parse_string(input_string):
    result = []
    matches = re.findall(r'define\s+(-?\d+)\s+=>\s*q\((.+?)\)', input_string)
    for match in matches:
        result.append((match[1], int(match[0])))
    return result


print(parse_string("<section>| define 971=> q(quanla_662). |; | define -7444 => q(veve).|; | define -7599 => q(aonve). |; </section>"))