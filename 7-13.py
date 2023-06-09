def main(data):
    H2, H3, H4, H5, H6 = 0, 0, 0, 0, 0
    for name, value in data:
        if name == 'H2':
            H2 = int(value)
        elif name == 'H3':
            H3 = int(value)
        elif name == 'H4':
            H4 = int(value)
        elif name == 'H5':
            H5 = int(value)
        elif name == 'H6':
            H6 = int(value)

    result = (H6 << 34) | (H5 << 25) | (H4 << 19) | (H3 << 18) | (H2 << 9)
    return str(result)