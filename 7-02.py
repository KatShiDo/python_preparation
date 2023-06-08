def main(hex_string: str) -> tuple:
    num = int(hex_string, 16)
    s1 = str(num & 0b1111111111)
    s2 = str((num >> 10) & 1)
    s3 = str((num >> 11) & 1)
    s4 = str((num >> 12) & 0b11)
    return (s1, s2, s3, s4)

print(main('0x31ca'))