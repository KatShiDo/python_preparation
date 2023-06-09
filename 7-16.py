def main(data):
    data = int(data, 16)
    Q1 = (data >> 0) & 0x1f
    Q2 = (data >> 5) & 0x1f
    Q4 = (data >> 18) & 0x3ff

    result = [('Q1', hex(Q1)), ('Q2', hex(Q2)), ('Q4', hex(Q4))]
    return result