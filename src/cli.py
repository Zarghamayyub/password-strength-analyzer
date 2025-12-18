import argparse
from analyzer import PasswordAnalyzer


def main():
    parser = argparse.ArgumentParser(
        description="Password Strength Analyzer - CLI Tool"
    )

    parser.add_argument(
        "-p", "--password",
        help="Password string to analyze"
    )

    parser.add_argument(
        "-f", "--file",
        help="Path to file containing passwords (one per line)"
    )

    args = parser.parse_args()

    analyzer = PasswordAnalyzer(dictionary_path="../data/dictionary.txt")

    if args.password:
        result = analyzer.score_password(args.password)
        display_result(args.password, result)

    elif args.file:
        try:
            with open(args.file, "r", encoding="utf-8") as f:
                for line in f:
                    pwd = line.strip()
                    if pwd:
                        result = analyzer.score_password(pwd)
                        display_result(pwd, result)
        except FileNotFoundError:
            print("Error: File not found.")

    else:
        print("No input provided. Use --password or --file.")


def display_result(password, result):
    print("=" * 40)
    print(f"Password: {password}")
    print(f"Score: {result['score']}")
    print(f"Strength: {result['strength']}")

    if result["details"]["patterns"]:
        print("Warnings:")
        for p in result["details"]["patterns"]:
            print(f" - {p}")

    if result["details"]["dictionary_word"]:
        print(" - Dictionary word detected")

    print("=" * 40)


if __name__ == "__main__":
    main()
