def main(data):
    data = int(data)
    Z1 = (data >> 0) & 0x1
    Z2 = (data >> 1) & 0xff
    Z3 = (data >> 9) & 0x1f
    Z4 = (data >> 14) & 0x3

    result = (Z1 << 15) | (Z3 << 10) | (Z2 << 2) | (Z4 << 0)
    return hex(result)