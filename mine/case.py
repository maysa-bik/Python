import tkinter as tk

class Case:
    def __init__(self, master, row, col, grid, game):
        self.master = master
        self.row = row
        self.col = col
        self.grid = grid
        self.game = game
        self.is_mine = False
        self.is_revealed = False
        self.adjacent_mines = 0

        self.button = tk.Button(master, text="", width=2, height=1, command=self.left_click)
        self.button.grid(row=row, column=col)

    def left_click(self):
        if not self.is_revealed:
            self.reveal()

    def reveal(self):
        if self.is_revealed or self.game.game_over:
            return
        self.is_revealed = True
        if self.is_mine:
            self.button.config(text="X", state="disabled")
            self.game.end_game()
        elif self.adjacent_mines == 0:
            self.button.config(text="", state="disabled")
            for dr in range(-1, 2):
                for dc in range(-1, 2):
                    r, c = self.row + dr, self.col + dc
                    if 0 <= r < len(self.grid) and 0 <= c < len(self.grid[0]):
                        self.grid[r][c].reveal()
        else:
            self.button.config(text=str(self.adjacent_mines), state="disabled")
