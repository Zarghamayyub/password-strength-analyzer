import math
import re

class PasswordAnalyzer:

    def __init__(self, dictionary_path=None):
        self.dictionary = set()

        if dictionary_path:
            try:
                with open(dictionary_path, "r", encoding="utf-8") as f:
                    self.dictionary = {word.strip().lower() for word in f.readlines()}
            except FileNotFoundError:
                print("[WARNING] Dictionary file not found. Dictionary check disabled.")

    # -------------------------------------
    # 1. Character Variety Check
    # -------------------------------------
    def character_variety(self, password):
        lower = any(c.islower() for c in password)
        upper = any(c.isupper() for c in password)
        digits = any(c.isdigit() for c in password)
        symbols = any(not c.isalnum() for c in password)

        score = sum([lower, upper, digits, symbols]) * 10

        return score, {
            "lowercase": lower,
            "uppercase": upper,
            "digits": digits,
            "symbols": symbols
        }

    # -------------------------------------
    # 2. Entropy Calculation
    # -------------------------------------
    def calculate_entropy(self, password):
        charset = 0

        if any(c.islower() for c in password):
            charset += 26
        if any(c.isupper() for c in password):
            charset += 26
        if any(c.isdigit() for c in password):
            charset += 10
        if any(not c.isalnum() for c in password):
            charset += 32   # symbols approx.

        if charset == 0:
            return 0

        entropy = len(password) * math.log2(charset)
        return round(entropy, 2)

    # -------------------------------------
    # 3. Pattern Detection
    # -------------------------------------
    def detect_patterns(self, password):
        patterns = []

        # Sequential numbers
        if re.search(r"123|234|345|456|567|678|789|890", password):
            patterns.append("Sequential numbers detected")

        # Repeated characters
        if re.search(r"(.)\1{2,}", password):
            patterns.append("Repeated characters detected")

        # Keyboard patterns
        keyboard_patterns = ["qwerty", "asdf", "zxcv", "pass", "admin"]
        for key in keyboard_patterns:
            if key in password.lower():
                patterns.append(f"Keyboard/common pattern: {key}")

        return patterns

    # -------------------------------------
    # 4. Dictionary Word Check
    # -------------------------------------
    def dictionary_check(self, password):
        if not self.dictionary:
            return False

        password_lower = password.lower()
        return any(word in password_lower for word in self.dictionary)

    # -------------------------------------
    # 5. Final Scoring System
    # -------------------------------------
    def score_password(self, password):
        score = 0
        details = {}

        # Length score
        length_score = min(len(password) * 5, 30)   # Max 30
        score += length_score
        details["length_score"] = length_score

        # Variety
        variety_score, variety = self.character_variety(password)
        score += variety_score
        details["variety"] = variety

        # Entropy
        entropy = self.calculate_entropy(password)
        entropy_score = min(int(entropy), 30)  # Max 30
        score += entropy_score
        details["entropy"] = entropy

        # Patterns
        patterns = self.detect_patterns(password)
        if patterns:
            score -= 10 * len(patterns)
        details["patterns"] = patterns

        # Dictionary penalty
        if self.dictionary_check(password):
            score -= 20
            details["dictionary_word"] = True
        else:
            details["dictionary_word"] = False

        # Final clamp
        score = max(0, min(score, 100))

        # Strength label
        if score < 30:
            strength = "Weak"
        elif score < 60:
            strength = "Medium"
        elif score < 80:
            strength = "Strong"
        else:
            strength = "Very Strong"

        return {
            "score": score,
            "strength": strength,
            "details": details
        }
