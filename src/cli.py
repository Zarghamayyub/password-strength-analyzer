from analyzer import analyze_password, improvement_suggestions

def main():
    print("=== Password Strength Analyzer (CLI) ===")
    password = input("Enter password: ")

    score = analyze_password(password)
    print(f"\nPassword Strength Score: {score}%")

    if score < 40:
        print("Strength Level: Weak")
    elif score < 70:
        print("Strength Level: Medium")
    else:
        print("Strength Level: Strong")

    suggestions = improvement_suggestions(password)

    if suggestions:
        print("\nImprovement Suggestions:")
        for s in suggestions:
            print(f"- {s}")
    else:
        print("\nStrong password. No improvements needed.")


if __name__ == "__main__":
    main()
