import tkinter as tk
import numpy as np
from tkinter import ttk
import time

class SudokuGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Sudoku")

        self.frame = ttk.Frame(master, padding=20)
        self.frame.grid(column=0, row=0, columnspan=9, rowspan=12) # Adjusted columnspan/rowspan

        self.grid_size = 9
        self.entries = []
        self.str_vars = [] # To hold StringVar objects for each entry

        self._create_widgets()
        self._start_time = time.time()
        self._update_timer()

    def _create_widgets(self):
        # Title
        ttk.Label(self.frame, text="SUDOKU", font=('Arial', 24)).grid(column=0, row=0, columnspan=self.grid_size)
        
        # Entry boxes
        for i in range(self.grid_size):
            row_entries = []
            row_str_vars = []
            for j in range(self.grid_size):
                str_var = tk.StringVar()
                str_var.trace_add("write", lambda name, index, mode, sv=str_var: self._validate_input(sv))
                row_str_vars.append(str_var)
                
                # Add some visual separation for 3x3 boxes
                padx = (5, 0) if (j + 1) % 3 == 1 and j != self.grid_size - 1 else (0, 0)
                pady = (5, 0) if (i + 1) % 3 == 1 and i != self.grid_size - 1 else (0, 0)

                entr = ttk.Entry(self.frame, width=3, font=('Arial', 20),
                                 textvariable=str_var, justify='center')
                entr.grid(row=i + 1, column=j, padx=padx, pady=pady) # Offset by 1 for title
                row_entries.append(entr)
            self.entries.append(row_entries)
            self.str_vars.append(row_str_vars)

        # Result message label
        self.result_label = ttk.Label(self.frame, text="", font=('Arial', 14))
        self.result_label.grid(column=0, row=self.grid_size + 1, columnspan=self.grid_size, pady=10)

        # Buttons
        ttk.Button(self.frame, text="Check", command=self._check_sudoku).grid(column=0, row=self.grid_size + 2, columnspan=self.grid_size // 2, pady=5)
        ttk.Button(self.frame, text="Quit", command=self.master.destroy).grid(column=self.grid_size // 2, row=self.grid_size + 2, columnspan=self.grid_size // 2, pady=5)

        # Timer label
        self.timer_var = tk.StringVar()
        self.timer_label = ttk.Label(self.frame, textvariable=self.timer_var, font=('Arial', 12))
        self.timer_label.grid(column=0, row=self.grid_size + 3, columnspan=self.grid_size, pady=5)


    def _validate_input(self, string_var):
        """Ensures only digits 1-9 are entered and limits to one character."""
        content = string_var.get()
        if not content.isdigit() and content != '':
            string_var.set(''.join(filter(str.isdigit, content)))
        if len(string_var.get()) > 1:
            string_var.set(string_var.get()[0])
        if content != '' and (int(content) < 1 or int(content) > 9):
            string_var.set('')

    def _get_current_values(self):
        """
        Extracts values from entry boxes and returns them as a 9x9 numpy array.
        Returns None if any entry is empty or invalid.
        """
        board = np.zeros((self.grid_size, self.grid_size), dtype=int)
        for r in range(self.grid_size):
            for c in range(self.grid_size):
                val_str = self.str_vars[r][c].get()
                if not val_str.isdigit():
                    return None # Indicates invalid input
                board[r, c] = int(val_str)
        return board

    def _check_rules(self, data):
        """
        Checks if a given row, column, or 3x3 block satisfies Sudoku rules.
        Returns True if valid, False otherwise.
        """
        # Convert to set to easily check for duplicates and presence of 1-9
        seen = set()
        for x in data:
            if x < 1 or x > 9: # Ensure numbers are within 1-9 range
                return False
            if x in seen:
                return False # Duplicate found
            seen.add(x)
        
        # Check if all numbers from 1 to 9 are present
        if len(seen) != self.grid_size: # Should be 9 unique numbers if complete
            return False
        return True

    def _check_sudoku_logic(self):
        """
        Checks if the current entries satisfy the rules of Sudoku.
        Returns:
            True: If the Sudoku is valid.
            "invalid_char": If any non-digit or out-of-range character is found.
            "row_error": If a row rule is violated.
            "col_error": If a column rule is violated.
            "box_error": If a 3x3 box rule is violated.
        """
        board = self._get_current_values()
        if board is None:
            return "invalid_char"

        # Check rows
        for r in range(self.grid_size):
            if not self._check_rules(board[r, :]):
                return "row_error"

        # Check columns
        for c in range(self.grid_size):
            if not self._check_rules(board[:, c]):
                return "col_error"

        # Check 3x3 boxes
        box_size = int(np.sqrt(self.grid_size)) # Should be 3 for a 9x9 grid
        for i in range(box_size):
            for j in range(box_size):
                sub_matrix = board[i * box_size : (i + 1) * box_size,
                                   j * box_size : (j + 1) * box_size].flatten()
                if not self._check_rules(sub_matrix):
                    return "box_error"
        
        return True

    def _check_sudoku(self):
        """Updates the result label based on Sudoku logic check."""
        result = self._check_sudoku_logic()

        messages = {
            True: "You Win! Congratulations!",
            "invalid_char": "Please use only digits 1-9 in the cells.",
            "row_error": "There's a mistake in one of your rows.",
            "col_error": "There's a mistake in one of your columns.",
            "box_error": "There's a mistake in one of your 3x3 boxes.",
            "error": "An unexpected error occurred." 
        }
        self.result_label.config(text=messages.get(result, messages["error"]))

    def _update_timer(self):
        """Updates the elapsed time displayed on the timer label."""
        elapsed_time = int(time.time() - self._start_time)
        self.timer_var.set(f"Time Elapsed: {elapsed_time // 60:02d}:{elapsed_time % 60:02d}")
        self.master.after(1000, self._update_timer) # Update every 1 second

if __name__ == "__main__":
    root = tk.Tk()
    game = SudokuGame(root)
    root.mainloop()
