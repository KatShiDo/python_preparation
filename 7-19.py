def main(data):
    data = int(data, 16)
    L1 = (data >> 0) & 0xff
    L2 = (data >> 8) & 0x1
    L3 = (data >> 9) & 0x1f
    L5 = (data >> 19) & 0x1

    result = {'L1': hex(L1), 'L2': hex(L2), 'L3': hex(L3), 'L5': hex(L5)}
    return result