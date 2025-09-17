def missing_statues(sizes):
    if not sizes:
        return 0

    min_size = sizes[0]
    max_size = sizes[0]

    for size in sizes:
        min_size = min(min_size, size)
        max_size = max(max_size, size)

    total_statues = max_size - min_size + 1
    unique_sizes = set(sizes)

    missing = total_statues - len(unique_sizes)
    return missing
