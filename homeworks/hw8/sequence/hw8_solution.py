def ascending_sequence(sequence):
    count = 0
    for i in range(1, len(sequence)):
        if sequence[i] <= sequence[i - 1]:
            count += 1
            if count > 1:
                return False
            if i > 1 and i < len(sequence) - 1 and sequence[i] <= sequence[i - 2] and sequence[i + 1] <= sequence[i - 1]:
                return False
    return True
