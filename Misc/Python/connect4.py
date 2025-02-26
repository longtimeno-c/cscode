import tkinter as tk
from tkinter import messagebox

# Game constants
ROWS = 6
COLS = 7
PLAYER_COLORS = {1: "red", 2: "yellow"}

class Connect4Game:
    def __init__(self, root):
        self.root = root
        self.root.title("Connect 4")

        self.board = [[0] * COLS for _ in range(ROWS)]
        self.current_player = 1  # Player 1 starts
        
        # UI Elements
        self.canvas = tk.Canvas(root, width=COLS*100, height=ROWS*100, bg="blue")
        self.canvas.grid(row=0, column=0, columnspan=COLS)

        self.buttons = []
        for col in range(COLS):
            btn = tk.Button(root, text=f"↓", font=("Arial", 18), command=lambda c=col: self.drop_piece(c))
            btn.grid(row=1, column=col)
            self.buttons.append(btn)

        self.draw_board()

    def draw_board(self):
        """Draws the game board"""
        self.canvas.delete("all")
        for row in range(ROWS):
            for col in range(COLS):
                x0, y0 = col * 100 + 10, row * 100 + 10
                x1, y1 = (col + 1) * 100 - 10, (row + 1) * 100 - 10
                color = "white" if self.board[row][col] == 0 else PLAYER_COLORS[self.board[row][col]]
                self.canvas.create_oval(x0, y0, x1, y1, fill=color, outline="black")

    def drop_piece(self, col):
        """Handles dropping a piece into the selected column"""
        for row in reversed(range(ROWS)):  # Start from the bottom
            if self.board[row][col] == 0:
                self.board[row][col] = self.current_player
                self.draw_board()
                if self.check_win(row, col):
                    messagebox.showinfo("Game Over", f"Player {self.current_player} ({PLAYER_COLORS[self.current_player]}) wins!")
                    self.disable_buttons()
                    return
                self.current_player = 3 - self.current_player  # Swap players (1 -> 2, 2 -> 1)
                return
        messagebox.showwarning("Column Full", "That column is full! Choose another.")

    def check_win(self, row, col):
        """Checks if the current move resulted in a win"""
        def count_streak(dx, dy):
            """Count pieces in a given direction"""
            r, c, count = row, col, 0
            while 0 <= r < ROWS and 0 <= c < COLS and self.board[r][c] == self.current_player:
                count += 1
                r += dx
                c += dy
            return count

        # Check all four directions
        directions = [(1, 0), (0, 1), (1, 1), (1, -1)]
        for dx, dy in directions:
            if count_streak(dx, dy) + count_streak(-dx, -dy) - 1 >= 4:
                return True
        return False

    def disable_buttons(self):
        """Disables all buttons after the game ends"""
        for btn in self.buttons:
            btn.config(state=tk.DISABLED)

# Run the game
if __name__ == "__main__":
    root = tk.Tk()
    game = Connect4Game(root)
    root.mainloop()