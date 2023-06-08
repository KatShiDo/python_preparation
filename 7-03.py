def main(num: int) -> tuple:
    u1 = num & 0b111111111
    u3 = (num >> 13) & 0b11111
    u4 = (num >> 18) & 0b111111
    return u1, u3, u4


print(main(1102195))
