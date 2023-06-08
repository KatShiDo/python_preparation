def main(hex_string: str) -> tuple:
    num = int(hex_string, 16)
    h1 = hex(num & 0b111111111)
    h2 = hex((num >> 9) & 0b1111111)
    h3 = hex((num >> 16) & 0b1111)
    h4 = hex((num >> 20) & 0b1111111)
    return h1, h2, h3, h4


print(main('0x1ccdc81'))