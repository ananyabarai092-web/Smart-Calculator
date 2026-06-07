# Smart Calculator CLI

A professional, terminal-first Smart Calculator built in Python. This project demonstrates modular design, clean code, file persistence, user profiles, and a polished command-line UI — suitable for GitHub, portfolios, and resume projects.

---

## Features

- Fully modular architecture (see `main.py`, `calculator.py`, `history.py`, `profiles.py`).
- Basic arithmetic: addition, subtraction, multiplication, division.
- Advanced tools: power, modulus, square root, percentage, factorial, average.
- Utility calculators: BMI and EMI (loan) calculator.
- Scientific operations: `sin`, `cos`, `tan`, `log` (base 10), `ln`, `exp`, `sqrt`.
- Memory functions: `M+`, `M-`, `MR`, `MC`.
- Random number generator with user-defined range.
- Persistent calculation history saved to `history.json` with search, delete and clear operations.
- User profiles with badges, stored in `users.json`.
- Theme support (Dark / Light) using `colorama` for a modern terminal UI.
- Robust input validation and exception handling.

---

## Quick Start

1. Clone the repository (or download the source files).

```bash
git clone https://github.com/<your-username>/smart-calculator-cli.git
cd smart-calculator-cli
```

2. Create a Python virtual environment and install dependencies.

```bash
python -m venv .venv
.venv\\Scripts\\activate   # Windows
pip install -r requirements.txt
```

3. Run the application.

```bash
python main.py
```

---

## Files and Structure

- `main.py` — Entry point and CLI menu system.
- `calculator.py` — All mathematical operations and memory functions.
- `history.py` — JSON persistence helpers for calculation history.
- `statistics.py` — Functions to generate the dashboard metrics.
- `achievements.py` — Badge logic for user profiles.
- `profiles.py` — User registration, login and profile updates.
- `utils.py` — Terminal helpers, theme control, input prompts.
- `history.json` — Persistent history (ignored from git by default).
- `users.json` — User profiles storage (ignored from git by default).

---

## Usage Examples

- Addition (multiple values): Enter comma-separated numbers when prompted.
- Division: attempting `10 / 0` returns a friendly error: `Error: Division by zero is not allowed.`
- BMI: provide weight (kg) and height (m) to get numeric BMI and a category.

The program always stores calculations in `history.json` with a timestamp and optional user.

---

## Configuration & Best Practices

- `history.json` and `users.json` are added to `.gitignore` by default to avoid committing user data. Use `history.example.json` and `users.example.json` if you want sample data in the repo.
- Use the virtual environment `.venv` during development to isolate dependencies.

---

## Contributing

1. Fork the repo and create a feature branch.
2. Run tests and linters locally (add tests as you extend the project).
3. Open a pull request with a clear description of changes.

---

## License

Choose a license (MIT, Apache-2.0, etc.) and add a `LICENSE` file before publishing.

---

## Contact

Open an issue or create a pull request on the GitHub repository for feedback or feature requests.

Thank you for using Smart Calculator — a portfolio-ready Python CLI utility.
