def main(bit_fields: dict) -> str:
    m1 = int(bit_fields['M1'])
    m2 = int(bit_fields['M2'])
    m3 = int(bit_fields['M3'])
    m4 = int(bit_fields['M4'])
    m5 = int(bit_fields['M5'])
    result = (m1 << 0) | (m2 << 9) | (m3 << 19) | (m4 << 22) | (m5 << 28)
    return str(result)


print(main({'M1': '119', 'M2': '90', 'M3': '6', 'M4': '45', 'M5': '112'}))