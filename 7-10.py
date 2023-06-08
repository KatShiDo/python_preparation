def main(bit_fields: tuple) -> str:
    s1 = int(bit_fields[0], 16)
    s2 = int(bit_fields[1], 16)
    s3 = int(bit_fields[2], 16)
    s4 = int(bit_fields[3], 16)
    result = (s1 << 0) | (s2 << 1) | (s3 << 10) | (s4 << 14)
    return str(result)


print(main(('0x1', '0x1a6', '0xd', '0x6')))