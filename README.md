# NYT Spelling Bee Solver

## Description
This Python project automates the process of extracting letters from the **NYT Spelling Bee** game and finds all valid words based on the rules of the game:
1. Words must include the "important letter" (the first letter in the list).
2. Words must be at least 4 letters long.
3. Words can only use the given letters, and letters can repeat.

The project uses Selenium to scrape the game and the NLTK library for word validation.

---

## Features
- Automates interaction with the **NYT Spelling Bee** game.
- Dynamically fetches the letter set for the current puzzle.
- Finds all valid words that meet the game rules.

---

## Requirements
- **Python >= 3.9**
- **Google Chrome**
- **ChromeDriver** (matching your Chrome version) Use this link for versions above 115: https://googlechromelabs.github.io/chrome-for-testing/

---

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/gitedmond/nyt-spelling-bee-solver.git
cd nyt-spelling-bee-solver
