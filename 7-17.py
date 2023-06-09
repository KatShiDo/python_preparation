def main(data):
    data = int(data, 16)
    J1 = (data >> 0) & 0x1f
    J3 = (data >> 12) & 0x7
    J4 = (data >> 15) & 0x1ff

    result = (J3 << 21) | (J4 << 12) | (J1 << 0)
    return hex(result)