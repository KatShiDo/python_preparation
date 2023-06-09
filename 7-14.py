def main(data):
    data = int(data)
    X1 = (data >> 0) & 0xff
    X2 = (data >> 8) & 0x3
    X3 = (data >> 10) & 0x7f
    X4 = (data >> 17) & 0x1

    result = (X2 << 16) | (X4 << 15) | (X3 << 8) | (X1 << 0)
    return hex(result)