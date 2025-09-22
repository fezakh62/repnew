def is_card_number_valid(number):
    try:
        digits = [int(d) for d in str(number)]
    except ValueError:
        return False

    if not digits:
        return False

    total = 0
    double = False

    for d in reversed(digits):
        val = d * 2 if double else d
        if val > 9:
            val -= 9
        total += val
        double = not double

    return total % 10 == 0
