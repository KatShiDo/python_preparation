def main(decimal_string: str) -> dict:
    num = int(decimal_string)
    w1 = str(num & 0b1111111)
    w2 = str((num >> 7) & 0b11111)
    w3 = str((num >> 12) & 0b11111)
    w4 = str((num >> 17) & 0b1111)
    w5 = str((num >> 21) & 0b11)
    return {'W1': w1, 'W2': w2, 'W3': w3, 'W4': w4, 'W5': w5}


print(main('7758057'))
