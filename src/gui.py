import tkinter as tk
from tkinter import messagebox
from analyzer import PasswordAnalyzer


class PasswordAnalyzerGUI:

    def __init__(self, root):
        self.root = root
        self.root.title("Password Strength Analyzer")
        self.root.geometry("500x400")
        self.root.resizable(False, False)

        self.analyzer = PasswordAnalyzer(dictionary_path="../data/dictionary.txt")

        # Title
        title = tk.Label(
            root,
            text="Password Strength Analyzer",
            font=("Arial", 16, "bold")
        )
        title.pack(pady=10)

        # Password input
        frame = tk.Frame(root)
        frame.pack(pady=10)

        label = tk.Label(frame, text="Enter Password:")
        label.pack(side=tk.LEFT, padx=5)

        self.password_entry = tk.Entry(frame, width=30, show="*")
        self.password_entry.pack(side=tk.LEFT)

        # Analyze button
        analyze_btn = tk.Button(
            root,
            text="Analyze Password",
            command=self.analyze_password
        )
        analyze_btn.pack(pady=10)

        # Output box
        self.output = tk.Text(root, height=12, width=55)
        self.output.pack(pady=10)
        self.output.config(state=tk.DISABLED)

    def analyze_password(self):
        password = self.password_entry.get()

        if not password:
            messagebox.showwarning("Input Error", "Please enter a password.")
            return

        result = self.analyzer.score_password(password)

        self.output.config(state=tk.NORMAL)
        self.output.delete("1.0", tk.END)

        self.output.insert(tk.END, f"Password Score: {result['score']}\n")
        self.output.insert(tk.END, f"Strength: {result['strength']}\n\n")

        if result["details"]["patterns"]:
            self.output.insert(tk.END, "Warnings:\n")
            for p in result["details"]["patterns"]:
                self.output.insert(tk.END, f" - {p}\n")

        if result["details"]["dictionary_word"]:
            self.output.insert(tk.END, " - Dictionary word detected\n")

        self.output.config(state=tk.DISABLED)


if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordAnalyzerGUI(root)
    root.mainloop()
