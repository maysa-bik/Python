import tkinter as tk
import time
from grille import Grille

class MineSweeperGUI:
    def __init__(self, master, difficulty="medium"):
        self.master = master
        self.difficulty = difficulty
        self.rows, self.cols, self.num_mines = self.set_difficulty()
        self.game_started = False
        self.game_over = False
        self.start_time = None
        self.timer_label = None

        self.create_widgets()
        self.start_game()

    def set_difficulty(self):
        if self.difficulty == "easy":
            return 8, 8, 10
        elif self.difficulty == "medium":
            return 16, 16, 40
        elif self.difficulty == "hard":
            return 16, 30, 99
        else:
            return 16, 30, 40  # Default to medium difficulty

    def create_widgets(self):
        self.grille = Grille(self.master, self.rows, self.cols, self.num_mines, self)
        self.grille.create_board()  # Correction: Utilise create_board() au lieu de place_board()

        self.restart_button = tk.Button(self.master, text="Restart", command=self.restart_game)
        self.restart_button.grid(row=self.rows, columnspan=self.cols, sticky="we")

        self.timer_label = tk.Label(self.master, text="Time: 0")
        self.timer_label.grid(row=self.rows + 1, columnspan=self.cols, sticky="we")

    def start_game(self):
        self.start_time = time.time()
        self.game_started = True

    def end_game(self):
        self.game_over = True
        elapsed_time = round(time.time() - self.start_time, 2)
        print("Game Over!")
        print(f"Elapsed Time: {elapsed_time} seconds")

    def restart_game(self):
        self.game_over = False
        self.game_started = False
        self.start_time = None
        self.timer_label.config(text="Time: 0")
        self.grille.restart()

        if not self.game_started:
            self.start_game()

    def update_timer(self):
        if not self.game_over and self.game_started:
            elapsed_time = int(time.time() - self.start_time)
            self.timer_label.config(text=f"Time: {elapsed_time}")
            self.master.after(1000, self.update_timer)

root = tk.Tk()
game_gui = MineSweeperGUI(root, difficulty="medium")  # Change difficulty here
game_gui.update_timer()
root.mainloop()
