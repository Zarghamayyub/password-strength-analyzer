# Password Strength Analyzer (CLI + GUI)

## Overview
The Password Strength Analyzer is a cybersecurity-focused Python application designed to evaluate password security using multiple analytical techniques. Unlike basic validators, this project combines rule-based analysis, dictionary detection, entropy estimation, and real-time feedback through both Command Line Interface (CLI) and Graphical User Interface (GUI).

This project is intended for educational, defensive security, and portfolio demonstration purposes.

---

## Key Features
- Dual Interface Support (CLI & GUI)
- Password length and complexity analysis
- Dictionary-based weak password detection
- Entropy-based strength scoring
- Real-time strength feedback
- Color-coded results (GUI)
- Unit testing support
- Modular and extensible architecture

---

## Project Structure
password-strength-analyzer/
│
├── src/
│ ├── analyzer.py # Core analysis logic
│ ├── cli.py # Command-line interface
│ └── gui.py # GUI interface
│
├── tests/
│ └── test_analyzer.py # Unit tests
│
├── data/
│ └── dictionary.txt # Weak password dictionary
│
├── docs/
│ └── architecture.md # Project architecture
│
├── requirements.txt
├── test_run.py
└── README.md

yaml
Copy code

---

## Installation
```bash
git clone https://github.com/zarghamayyub/password-strength-analyzer.git
cd password-strength-analyzer
pip install -r requirements.txt
Usage
CLI Mode
bash
Copy code
python src/cli.py
GUI Mode
bash
Copy code
python src/gui.py
Password Scoring Criteria
Score Range	Strength Level
0 – 39	Weak
40 – 69	Medium
70 – 100	Strong

Technologies Used
Python 3

Tkinter (GUI)

Pytest

Object-Oriented Programming

Secure Coding Practices

Future Enhancements
Breached password API integration

Password policy export feature

Multi-language GUI support

Strength comparison analytics

Disclaimer
This project is for educational and defensive cybersecurity purposes only.
It does not store or transmit passwords.

Author
Zargham Ayyub
Cybersecurity | Python | Secure Software Development

yaml
Copy code

---

## 🔷 NEXT ACTION (VERY SIMPLE)

1. Open `README.md` in VS Code  
2. **Replace all content** with above README  
3. Save file  
4. Run:
```bash
git add README.md
git commit -m "Improved README with professional documentation"
git push