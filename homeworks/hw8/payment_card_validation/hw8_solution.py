def is_card_number_valid(number):
    if not str(number).isdigit():
        return False

    digits = [int(d) for d in str(number)]
    checksum = 0

    for i, d in enumerate(reversed(digits)):
        if i % 2 == 1:
            d *= 2
            if d > 9:
                d -= 9
        checksum += d

    return checksum % 10 == 0
