def print_fibonacci(length):
    sequence = []

    if length > 0:
        sequence.append(0)
    if length > 1:
        sequence.append(1)

    while len(sequence) < length:
        sequence.append(sequence[-1] + sequence[-2])

    print(sequence)
