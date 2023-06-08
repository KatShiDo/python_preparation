def main(bit_fields: list) -> int:
    bit_field_dict = dict(bit_fields)
    h1 = int(bit_field_dict['H1'])
    h3 = int(bit_field_dict['H3'])
    h4 = int(bit_field_dict['H4'])
    result = (h1 << 0) | (h3 << 10) | (h4 << 12)
    return result


print(main([('H1', '115'), ('H3', '0'), ('H4', '103')]))