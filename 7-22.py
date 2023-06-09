def main(data):
    D1 = int(data['D1'])
    D2 = int(data['D2'])
    D4 = int(data['D4'])
    D5 = int(data['D5'])

    result = (D5 << 24) | (D4 << 20) | (D2 << 5) | (D1 << 0)
    return hex(result)