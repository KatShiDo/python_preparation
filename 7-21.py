def main(data):
    data = int(data)
    N1 = (data >> 0) & 0x3
    N2 = (data >> 2) & 0x1ff
    N4 = (data >> 21) & 0x3ff

    result = {'N1': N1, 'N2': N2, 'N4': N4}
    return result