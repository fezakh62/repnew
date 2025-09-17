def generate_secret_number():
    return "3219"


def check_guess(secret, guess):
    bulls = 0
    cows = 0
    for i in range(4):
        if guess[i] == secret[i]:
            bulls += 1
        elif guess[i] in secret:
            cows += 1
    return bulls, cows


print(generate_secret_number())
print(check_guess(generate_secret_number(), generate_secret_number()))
