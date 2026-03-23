# CodeWars Solutions

A collection of Python solutions to CodeWars kata challenges.

## Requirements

- Python 3.9.6

No external libraries needed — all solutions use Python's standard library.

## Setup

Clone the repository to your local machine:

```bash
git clone https://github.com/Des-4281/codewars_solutions.git
cd codewars_solutions
```

## Running a Solution Locally

Each solution can be run directly from the terminal. Since these are designed for CodeWars, you may need to add a temporary `input()` and `print()` call at the bottom to test locally:

```bash
python3 codewars_solutions.py
```

> **Note:** When submitting to CodeWars, remove any `input()` and `print()` calls — CodeWars calls your function directly with its own test values.

## Solutions Included

| Challenge | Function |
|---|---|
| Even or Odd | `even_or_odd(number)` |
| Remove String Spaces | `no_space(string)` |
| Count Vowels | `getCount(inputStr)` |

## Pushing Updates to GitHub

After adding new solutions, push them with:

```bash
export PATH=/usr/bin:$PATH
git add codewars_solutions.py
git commit -m "Add new solution"
git push origin main
```

> **Note:** The `export PATH` line is required on this machine to avoid a git/curl conflict. You can make it permanent by adding it to your `~/.zshrc` file.
