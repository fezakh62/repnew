def missing_statues(sizes):
    if len(sizes) == 0:
        return 0

    min_size = sizes[0]
    max_size = sizes[0]

    for size in sizes:
        if size < min_size:
            min_size = size
        if size > max_size:
            max_size = size

    total_statues = max_size - min_size + 1

    unique_sizes = set()
    for size in sizes:
        unique_sizes.add(size)

    missing = total_statues - len(unique_sizes)
    return missing
