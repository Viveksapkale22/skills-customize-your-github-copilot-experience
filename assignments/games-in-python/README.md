
# 🎮 Hangman — Games in Python

## 🎯 Objective

Build a console-based Hangman game that lets a player guess letters to reveal a hidden word before they run out of attempts.

## 📝 Tasks

### 🛠️ Task 1 — Core game

#### Description
Implement the Hangman game loop with word selection, input handling, and win/lose conditions.

#### Requirements
- Randomly select a secret word from a predefined list.
- Show current progress (e.g. `_ _ a _ _`).
- Accept single-letter guesses and ignore repeated guesses.
- Track and display the remaining incorrect attempts.
- End the game with a clear win or lose message.

### 🛠️ Task 2 — (Optional) Difficulty & polish

#### Description
Add optional difficulty levels, input validation, and nicer console output.

#### Requirements
- Implement at least two difficulty settings that change `max_incorrect`.
- Validate input (single alphabetical character, not previously guessed).

## 📦 Files included

- `starter-code.py` — starter code and scaffolding for the assignment
- `README.md` — this file

## 🚀 How to run

1. Make sure you have Python 3.8+ installed.
2. Run the starter code:

```bash
python3 starter-code.py
```

## 🎓 Learning outcomes

- Practice string manipulation, loops, and conditional logic in Python.
- Handle user input and maintain program state across iterations.

## Grading / Acceptance

The submission will be considered complete when the program meets all requirements under "Task 1 — Core game" and runs without errors from the command line.

If you'd like, I can also add a minimal reference solution in `solutions/` or expand the starter code to include function-based structure.
