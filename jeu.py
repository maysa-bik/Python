import tkinter as tk
from tkinter import messagebox
import time
import random

class Grid:
    def __init__(self, master, rows, cols, num_mines, game):
        self.master = master
        self.rows = rows
        self.cols = cols
        self.num_mines = num_mines
        self.game = game
        self.create_board()

    def create_board(self):
        self.grid = [[None] * self.cols for _ in range(self.rows)]
        self.place_mines()

    def place_mines(self):
        locations = random.sample([(r, c) for r in range(self.rows) for c in range(self.cols)], self.num_mines)
        for r, c in locations:
            self.grid[r][c] = Cell(self.master, r, c, self.grid, self.game)
            self.grid[r][c].is_mine = True
        for r in range(self.rows):
            for c in range(self.cols):
                if self.grid[r][c] is None:
                    self.grid[r][c] = Cell(self.master, r, c, self.grid, self.game)
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

    def toggle_edit_mode(self):
        for r in range(self.rows):
            for c in range(self.cols):
                if self.grid[r][c] is not None:
                    self.grid[r][c].toggle_edit_mode()

class Cell:
    def __init__(self, master, row, col, grid, game):
        self.master = master
        self.row = row
        self.col = col
        self.grid = grid
        self.game = game
        self.is_mine = False
        self.is_revealed = False
        self.is_flagged = False
        self.is_questioned = False
        self.adjacent_mines = 0

        self.button = tk.Button(master, text="", width=2, height=1, command=self.left_click)
        self.button.grid(row=row, column=col)
        self.button.bind("<Button-3>", self.right_click)

    def left_click(self, event=None):
        if self.game.edit_mode:
            self.toggle_mine()
        elif not self.is_revealed:
            self.reveal()

    def right_click(self, event=None):
        if not self.is_revealed:
            if not self.is_flagged and not self.is_questioned:
                self.is_flagged = True
                self.button.config(text="F")
                self.game.update_remaining_mines(-1)
            elif self.is_flagged:
                self.is_flagged = False
                self.is_questioned = True
                self.button.config(text="?")
                self.game.update_remaining_mines(1)
            elif self.is_questioned:
                self.is_questioned = False
                self.button.config(text="")
                self.game.update_remaining_mines(1)

    def reveal(self):
        if self.is_revealed or self.game.game_over:
            return
        self.is_revealed = True
        if self.is_mine:
            self.button.config(text="X", bg="red", state="disabled")
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

    def toggle_edit_mode(self):
        if self.is_mine:
            self.button.config(bg="SystemButtonFace")
            self.is_mine = False
            self.game.update_remaining_mines(1)
        else:
            self.button.config(bg="black")
            self.is_mine = True
            self.game.update_remaining_mines(-1)

    def toggle_mine(self):
        if self.is_mine:
            self.button.config(bg="SystemButtonFace")
            self.is_mine = False
        else:
            self.button.config(bg="black")
            self.is_mine = True

class MineSweeperGUI:
    def __init__(self, master):
        self.master = master
        self.difficulty = "medium"
        self.edit_mode = False
        self.rows, self.cols, self.num_mines = self.get_difficulty_settings()
        self.game_started = False
        self.game_over = False
        self.start_time = None
        self.timer_label = None
        self.flags_remaining = self.num_mines
        self.play_button = None
        self.difficulty_buttons = []

        self.create_widgets()

    def set_difficulty(self, difficulty):
        self.difficulty = difficulty
        for button in self.difficulty_buttons:
            button.config(state="normal")
        if self.difficulty == "easy":
            self.difficulty_buttons[0].config(state="disabled")
        elif self.difficulty == "medium":
            self.difficulty_buttons[1].config(state="disabled")
        elif self.difficulty == "hard":
            self.difficulty_buttons[2].config(state="disabled")
        self.rows, self.cols, self.num_mines = self.get_difficulty_settings()
        self.restart_game()

    def get_difficulty_settings(self):
        if self.difficulty == "easy":
            return 10, 10, 10
        elif self.difficulty == "medium":
            return 16, 16, 40
        elif self.difficulty == "hard":
            return 20, 20, 100
        else:
            return 16, 16, 40  # Default to medium difficulty

    def create_widgets(self):
        self.grid = Grid(self.master, self.rows, self.cols, self.num_mines, self)
        self.grid.create_board()

        self.restart_button = tk.Button(self.master, text="Rejouer", command=self.restart_game, state="disabled")
        self.restart_button.grid(row=self.rows + 1, column=0, columnspan=self.cols, sticky="we")

        self.timer_label = tk.Label(self.master, text="Temps: 0")
        self.timer_label.grid(row=self.rows + 2, columnspan=self.cols, sticky="we")

        self.remaining_mines_label = tk.Label(self.master, text=f"Mines restantes: {self.flags_remaining}")
        self.remaining_mines_label.grid(row=self.rows + 3, columnspan=self.cols, sticky="we")

        self.edit_button = tk.Button(self.master, text="Mode édition", command=self.toggle_edit_mode)
        self.edit_button.grid(row=self.rows + 4, column=0, columnspan=self.cols, sticky="we")

        for i, (difficulty, text) in enumerate([("easy", "Facile"), ("medium", "Moyen"), ("hard", "Difficile")]):
            button = tk.Button(self.master, text=text, command=lambda d=difficulty: self.set_difficulty(d))
            button.grid(row=self.rows + 5, column=i, sticky="we")
            self.difficulty_buttons.append(button)

        self.play_button = tk.Button(self.master, text="Jouer", command=self.start_game)
        self.play_button.grid(row=self.rows + 6, column=0, columnspan=self.cols, sticky="we")

    def start_game(self):
        self.play_button.config(state="disabled")
        self.restart_button.config(state="normal")
        self.start_time = time.time() if not self.game_started else self.start_time
        self.game_started = True
        self.update_timer()

    def end_game(self):
        self.game_over = True
        if self.start_time is not None:
            elapsed_time = round(time.time() - self.start_time, 2)
            messagebox.showinfo("Fin du jeu", f"Temps écoulé: {elapsed_time} secondes")
        self.restart_button.config(state="normal")

    def restart_game(self):
        self.game_over = False
        self.game_started = False
        self.start_time = None
        self.timer_label.config(text="Temps: 0")
        self.remaining_mines_label.config(text=f"Mines restantes: {self.num_mines}")
        self.grid.restart()
        self.play_button.config(state="normal")

    def update_timer(self):
        if not self.game_over and self.game_started:
            elapsed_time = int(time.time() - self.start_time)
            self.timer_label.config(text=f"Temps: {elapsed_time}")
            self.master.after(1000, self.update_timer)

    def toggle_edit_mode(self):
        self.edit_mode = not self.edit_mode
        self.edit_button.config(text="Mode jeu" if self.edit_mode else "Mode édition")

    def update_remaining_mines(self, change):
        self.flags_remaining += change
        self.remaining_mines_label.config(text=f"Mines restantes: {self.flags_remaining}")

class StartMenu(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.master.title("Démineur - Menu de Démarrage")
        self.pack(fill=tk.BOTH, expand=True)

        self.difficulties = ["Facile", "Moyen", "Difficile"]
        self.selected_difficulty = tk.StringVar()
        self.selected_difficulty.set(self.difficulties[1])

        self.create_widgets()

    def create_widgets(self):
        title_label = tk.Label(self, text="Démineur", font=("Helvetica", 24))
        title_label.pack(pady=20)

        difficulty_frame = tk.Frame(self)
        difficulty_frame.pack(pady=10)

        difficulty_label = tk.Label(difficulty_frame, text="Difficulté:")
        difficulty_label.grid(row=0, column=0)

        difficulty_menu = tk.OptionMenu(difficulty_frame, self.selected_difficulty, *self.difficulties)
        difficulty_menu.grid(row=0, column=1)

        start_button = tk.Button(self, text="Commencer le jeu", command=self.start_game)
        start_button.pack(pady=20)

    def start_game(self):
        difficulty = self.selected_difficulty.get()
        num_mines = {"Facile": 10, "Moyen": 40, "Difficile": 100}[difficulty]
        root = self.master
        root.destroy()
        game_root = tk.Tk()
        game_gui = MineSweeperGUI(game_root)
        game_root.mainloop()

root = tk.Tk()
start_menu = StartMenu(root)
root.mainloop()
