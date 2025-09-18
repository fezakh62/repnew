def infinity_loop(a, b):
    if a == b:
        return False
    if a > b:
        return False

    if abs(a - b) == 1:
        return True

    return False


print(infinity_loop(2, 6))  # False
print(infinity_loop(2, 3))  # True
