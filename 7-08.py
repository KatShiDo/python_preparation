def main(hex_string: str) -> str:
    num = int(hex_string, 16)
    w1 = (num >> 0) & 0b11
    w2 = (num >> 2) & 0b1111111111
    w4 = (num >> 20) & 0b11111
    result = (w4 << 0) | (w2 << 13) | (w1 << 23)
    return str(result)


print(main('0x1ab6d2b'))