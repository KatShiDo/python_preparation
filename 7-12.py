def main(input_string):
    input_int = int(input_string)
    T1 = input_int & 0b11111
    T2 = (input_int >> 5) & 0b111
    T3 = (input_int >> 8) & 0b111111
    T4 = (input_int >> 14) & 0b11
    return {'T1': T1, 'T2': T2, 'T3': T3, 'T4': T4}