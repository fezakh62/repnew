import random


def generate_secret_number():
    digits = list("0123456789")
    random.shuffle(digits)
    return ''.join(digits[:4])


def check_guess(secret, guess):
    bulls = 0
    cows = 0
    for i in range(4):
        if guess[i] == secret[i]:
            bulls += 1
        elif guess[i] in secret:
            cows += 1
    return bulls, cows


SECRET = generate_secret_number()

print(SECRET)
print(check_guess(SECRET, generate_secret_number()))
