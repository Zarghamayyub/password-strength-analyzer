import tkinter as tk
from analyzer import analyze_password, improvement_suggestions


def check_password():
    password = entry.get()
    score = analyze_password(password)

    result_label.config(text=f"Score: {score}%")

    if score < 40:
        level_label.config(text="Strength: Weak", fg="red")
    elif score < 70:
        level_label.config(text="Strength: Medium", fg="orange")
    else:
        level_label.config(text="Strength: Strong", fg="green")

    suggestions = improvement_suggestions(password)

    if suggestions:
        suggestions_label.config(
            text="Suggestions:\n" + "\n".join(suggestions),
            fg="black"
        )
    else:
        suggestions_label.config(
            text="Strong password. No improvements needed.",
            fg="green"
        )


root = tk.Tk()
root.title("Password Strength Analyzer")

tk.Label(root, text="Enter Password:").pack(pady=5)

entry = tk.Entry(root, show="*", width=30)
entry.pack(pady=5)

tk.Button(root, text="Analyze", command=check_password).pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack()

level_label = tk.Label(root, text="")
level_label.pack()

suggestions_label = tk.Label(root, text="", justify="left")
suggestions_label.pack(pady=10)

root.mainloop()
