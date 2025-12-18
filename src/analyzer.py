import math

COMMON_PASSWORDS = set()

try:
    with open("data/dictionary.txt", "r") as f:
        for line in f:
            COMMON_PASSWORDS.add(line.strip().lower())
except FileNotFoundError:
    pass


def calculate_entropy(password):
    pool = 0
    if any(c.islower() for c in password):
        pool += 26
    if any(c.isupper() for c in password):
        pool += 26
    if any(c.isdigit() for c in password):
        pool += 10
    if any(c in "!@#$%^&*()-_=+[]{};:'\",.<>/?|" for c in password):
        pool += 32

    if pool == 0:
        return 0

    return len(password) * math.log2(pool)


def analyze_password(password):
    score = 0

    if len(password) >= 12:
        score += 30
    elif len(password) >= 8:
        score += 15

    if any(c.islower() for c in password):
        score += 10
    if any(c.isupper() for c in password):
        score += 10
    if any(c.isdigit() for c in password):
        score += 10
    if any(c in "!@#$%^&*()-_=+[]{};:'\",.<>/?|" for c in password):
        score += 10

    if password.lower() in COMMON_PASSWORDS:
        score -= 30

    entropy = calculate_entropy(password)
    score += min(int(entropy), 20)

    score = max(0, min(score, 100))
    return score


def improvement_suggestions(password):
    suggestions = []

    if len(password) < 12:
        suggestions.append("Increase password length to at least 12 characters")

    if not any(c.isupper() for c in password):
        suggestions.append("Add uppercase letters")

    if not any(c.islower() for c in password):
        suggestions.append("Add lowercase letters")

    if not any(c.isdigit() for c in password):
        suggestions.append("Add numeric characters")

    if not any(c in "!@#$%^&*()-_=+[]{};:'\",.<>/?|" for c in password):
        suggestions.append("Add special characters")

    return suggestions
