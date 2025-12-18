# Password Strength Analyzer

A professional **Cybersecurity Password Strength Analyzer** built with Python. The project provides **both CLI and GUI interfaces** using a shared backend engine for accurate, consistent analysis.

## 🔐 Features

* Password scoring (0–100)
* Strength classification: Weak / Medium / Strong / Very Strong
* Entropy calculation
* Character variety analysis (lowercase, uppercase, digits, symbols)
* Pattern detection (sequential, repeated, keyboard/common words)
* Dictionary word detection
* **CLI tool** for automation and scripting
* **GUI application (Tkinter)** for desktop usage

## 🧠 Architecture

The project follows a clean separation of concerns:

* `analyzer.py` → Core analysis engine
* `cli.py` → Command Line Interface
* `gui.py` → Graphical User Interface

Both CLI and GUI reuse the same backend logic.

## 📁 Project Structure

```
password-strength-analyzer/
│
├── src/
│   ├── analyzer.py
│   ├── cli.py
│   ├── gui.py
│   └── __init__.py
│
├── data/
│   └── dictionary.txt
│
├── tests/
│   └── test_analyzer.py
│
├── docs/
│   └── architecture.md
│
├── test_run.py
├── README.md
├── requirements.txt
├── LICENSE
└── .gitignore
```

## ▶️ Usage

### 1️⃣ CLI Usage

Run from the `src` directory:

```bash
cd src
python cli.py --password "Admin@123"
```

Analyze passwords from a file:

```bash
python cli.py --file ../passwords.txt
```

### 2️⃣ GUI Usage

```bash
cd src
python gui.py
```

A desktop window will open for interactive password analysis.

## 🧪 Example Output

```
Score: 60
Strength: Medium
Warnings:
 - Dictionary word detected
```

## 🛠 Requirements

* Python 3.x
* No external libraries required (Tkinter included with Python)

## 📌 Use Cases

* Cybersecurity training and labs
* SOC analyst practice
* Password policy validation
* Academic and portfolio projects

## 📄 License

This project is licensed under the MIT License.

---

**Author:** Zargham Ayyub
