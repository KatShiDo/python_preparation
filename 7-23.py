def main(data):
    J1 = (data >> 0) & 0x7
    J2 = (data >> 3) & 0xff
    J3 = (data >> 11) & 0x1
    J4 = (data >> 12) & 0x7f

    result = (J2 << 11) | (J1 << 8) | (J3 << 7) | (J4 << 0)
    return result