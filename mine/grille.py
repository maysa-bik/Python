import random
from case import Case

class Grille:
    def __init__(self, master, rows, cols, num_mines, game):
        self.master = master
        self.rows = rows
        self.cols = cols
        self.num_mines = num_mines
        self.game = game
        self.create_board()

    def create_board(self):
        self.grid = [[None] * self.cols for _ in range(self.rows)]  # Crée une grille vide
        self.place_mines()

    def place_mines(self):
        locations = random.sample([(r, c) for r in range(self.rows) for c in range(self.cols)], self.num_mines)
        for r, c in locations:
            self.grid[r][c] = Case(self.master, r, c, self.grid, self.game)
            self.grid[r][c].is_mine = True
        for r in range(self.rows):
            for c in range(self.cols):
                if self.grid[r][c] is None:
                    self.grid[r][c] = Case(self.master, r, c, self.grid, self.game)
                    self.grid[r][c].adjacent_mines = self.count_adjacent_mines(r, c)

    def count_adjacent_mines(self, row, col):
        count = 0
        for dr in range(-1, 2):
            for dc in range(-1, 2):
                r, c = row + dr, col + dc
                if 0 <= r < self.rows and 0 <= c < self.cols and self.grid[r][c] is not None and self.grid[r][c].is_mine:
                    count += 1
        return count

    def restart(self):
        for r in range(self.rows):
            for c in range(self.cols):
                if self.grid[r][c] is not None:
                    self.grid[r][c].button.grid_forget()
        self.create_board()
