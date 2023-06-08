def main(decimal_string: str) -> int:
    num = int(decimal_string)
    w1 = num & 0b1111111111
    w2 = (num >> 10) & 0b11
    w3 = (num >> 12) & 0b11111
    w4 = (num >> 17) & 0b1111111
    w5 = (num >> 26) & 0b11111111
    result = (w5 << 0) | (w2 << 7) | (w3 << 9) | ((w4 & 1) << 16) | ((w4 >> 1) << 17) | (w1 << 23)
    return result


print(main('1451186064'))