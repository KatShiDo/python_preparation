def main(hex_string: str) -> list:
    num = int(hex_string, 16)
    t2 = (num >> 1) & 0b111111
    t3 = (num >> 7) & 0b1111111111
    t4 = (num >> 17) & 0b111111111
    return [('T2', t2), ('T3', t3), ('T4', t4)]


print(main('0x307911'))