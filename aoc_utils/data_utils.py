def get_data(data):
    with open(data, 'r') as f:
        lines = [line.strip() for line in f]

    return lines
