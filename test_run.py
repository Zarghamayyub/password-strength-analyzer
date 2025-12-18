from src.analyzer import PasswordAnalyzer

analyzer = PasswordAnalyzer(dictionary_path="data/dictionary.txt")

password = input("Enter password to test: ")

result = analyzer.score_password(password)

print("\nPassword Analysis Result:")
print("Score:", result["score"])
print("Strength:", result["strength"])
print("Details:", result["details"])

