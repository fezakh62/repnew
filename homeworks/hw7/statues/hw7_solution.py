def missing_statues(sizes):
    if not sizes:
        return 0

    min_size = min(sizes)
    max_size = max(sizes)

    total_statues = max_size - min_size + 1
    unique_sizes = set(sizes)

    missing = total_statues - len(unique_sizes)
    return missing
