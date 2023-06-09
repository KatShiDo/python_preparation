def main(data):
    C1, C2, C3, C4 = [int(x, 16) for x in data]
    result = (C4 << 15) | (C3 << 9) | (C2 << 3) | (C1 << 0)
    return hex(result)