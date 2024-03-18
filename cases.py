import random

class Case:
    def __init__(self, is_mine=False):
        self.is_mine = is_mine
        self.is_revealed = False
        self.adjacent_mines = 0
    
    def reveal(self):
        self.is_revealed = True
    
    def place_mine(self):
        self.is_mine = True
    
    def is_empty(self):
        return not self.is_mine
    
    def set_adjacent_mines(self, count):
        self.adjacent_mines = count
    
    def __str__(self):
        if self.is_revealed:
            if self.is_mine:
                return "*"
            elif self.is_empty():
                return " "
            else:
                return str(self.adjacent_mines)
        else:
            return "X"  # Case non révélée

class GameBoard:
    def __init__(self, rows, cols, num_mines):
        self.rows = rows
        self.cols = cols
        self.num_mines = num_mines
        self.board = [[Case() for _ in range(cols)] for _ in range(rows)]
        self.generate_mines()

    def generate_mines(self):
        positions = [(row, col) for row in range(self.rows) for col in range(self.cols)]
        mine_positions = random.sample(positions, self.num_mines)
        for row, col in mine_positions:
            self.board[row][col].place_mine()
        self.update_adjacent_mines()

    def update_adjacent_mines(self):
        for row in range(self.rows):
            for col in range(self.cols):
                if not self.board[row][col].is_mine:
                    count = self.count_adjacent_mines(row, col)
                    self.board[row][col].set_adjacent_mines(count)

    def count_adjacent_mines(self, row, col):
        count = 0
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                r, c = row + dr, col + dc
                if 0 <= r < self.rows and 0 <= c < self.cols and self.board[r][c].is_mine:
                    count += 1
        return count

    def reveal(self, row, col):
        if not self.board[row][col].is_revealed:
            self.board[row][col].reveal()
            if self.board[row][col].is_empty():
                for dr in [-1, 0, 1]:
                    for dc in [-1, 0, 1]:
                        if dr == 0 and dc == 0:
                            continue
                        r, c = row + dr, col + dc
                        if 0 <= r < self.rows and 0 <= c < self.cols:
                            self.reveal(r, c)

    def __str__(self):
        return '\n'.join([''.join([str(cell) for cell in row]) for row in self.board])


# Exemple d'utilisation
rows = 5
cols = 5
num_mines = 5

game_board = GameBoard(rows, cols, num_mines)
print(game_board)
