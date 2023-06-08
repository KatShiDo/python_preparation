import re


def main(x):
    r = r"\[\[\s*variable\s*list\(\s*([^)]*)\)\s*=>\s*([^.]*)"
    z = re.findall(r, x)
    ls2 = []
    for ints, key in z:
        ls = []
        for i in ints.split():
            if i == ".":
                continue
            ls.append(int(i))
        p = (key, ls)
        ls2.append(p)
    return ls2
