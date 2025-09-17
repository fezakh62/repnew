def missing_statues(sizes):
    if len(sizes) == 0:
        return 0

    min = sizes[0]
    max = sizes[0]

    for size in sizes:
        if size < min:
            min = size
        if size > max:
            max = size

    total_statues = max - min + 1

    unique_sizes = []
    for size in sizes:
        if size not in unique_sizes:
            unique_sizes.append(size)

    missing = total_statues - len(unique_sizes)
    return missing

print(missing_statues([1, 2, 3, 4]), missing_statues([1, 2, 3, 4]))
