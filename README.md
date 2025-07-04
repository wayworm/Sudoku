# Sudoku Game

This project is a Sudoku application built as a practice exercise, focusing on GUI development with Tkinter and implementing Sudoku game logic.

## Features

* **Sudoku Grid**: A 9x9 grid where users can input numbers directly into the cells.
* **Input Validation**: Cells only accept single digits from 1 to 9, providing immediate feedback for invalid entries.
* **Sudoku Rule Verification**: A "Check" button allows the user to verify if their current entries satisfy all Sudoku rules:
    * Each row must contain the digits 1-9 exactly once.
    * Each column must contain the digits 1-9 exactly once.
    * Each of the nine 3x3 sub-grids (boxes) must contain the digits 1-9 exactly once.
* **Feedback**: Provides specific messages to the user indicating whether the Sudoku is solved or if there's an error in a row, column, or 3x3 box, or due to invalid characters.
* **Game Timer**: Tracks and displays the elapsed time since the game started, formatted as minutes and seconds.
* **Visual Enhancements**: The grid includes subtle visual separators to highlight the 3x3 boxes, improving readability.

---

## Technologies

* Python:
* **GUI**: `tkinter` (Python's standard GUI library)
* **Logic**: `numpy` (for efficient array manipulation and board representation) and standard Python for rule checking and game flow.

---

## Project Structure & Logic

The application is structured using an **object-oriented approach** with a `SudokuGame` class, which encapsulates the GUI components and game logic.

The core logic involves:

1.  **Input Handling**: Using `tk.StringVar` for each cell to manage user input and trigger validation.
3.  **Rule Checking**: Implementing functions to verify the uniqueness and completeness of numbers (1-9) within:
    * Each row
    * Each column
    * Each 3x3 sub-grid
    This is efficiently done using Python `set` operations to detect duplicates and missing numbers.
4.  **Timer Management**: Utilizing the `time` module and `root.after()` for a non-blocking, real-time timer.

---

## How to Run

1.  **Prerequisites**: Ensure you have Python installed. You'll also need the `numpy` library.
    ```bash
    pip install numpy
    ```
2.  **Save the code**: Save the provided Python code as a `.py` file (e.g., `sudoku_app.py`).
3.  **Execute**: Run the script from your terminal:
    ```bash
    python sudoku_app.py
    ```
