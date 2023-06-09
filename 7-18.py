def main(data):
    S1, S2, S4 = [int(x) for x in data]
    result = (S4 << 12) | (S2 << 7) | (S1 << 0)
    return str(result)