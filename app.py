import tkinter as tk
from tkinter import messagebox
window = tk.Tk()
window.title("Kryžiukai Nuliukai")
# Kintamieji
current_player = "X"
board = [[" " for _ in range(3)] for _ in range(3)]
buttons = [[None for _ in range(3)] for _ in range(3)]

# Patikrina, ar kas nors laimejo
def check_winner():
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] != " ":
            return board[row][0]

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return board[0][col]

    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]

    return None

# Patikrina, ar lenta pilna
def is_board_full():
    for row in board:
        if " " in row:
            return False
    return True

# Funkcija, kuri atliekama kiekvieno mygtuko paspaudimo metu
def button_click(row, col):
    global current_player

    if board[row][col] == " " and not check_winner():
        # Atnaujiname lenta ir mygtuko teksta
        board[row][col] = current_player
        buttons[row][col].config(text=current_player)

        # Patikrinam, ar yra laimetojas
        winner = check_winner()
        if winner:
            messagebox.showinfo("Laimėtojas!", f"Žaidėjas {winner} laimėjo!")
            reset_board()
        elif is_board_full():
            messagebox.showinfo("Lygiosios", "Žaidimas baigėsi lygiosiomis!")
            reset_board()
        else:
            # Pakeicia žaidėją
            current_player = "O" if current_player == "X" else "X"

# Funkcija lentos atstatymui
def reset_board():
    global current_player, board

    current_player = "X"
    board = [[" " for _ in range(3)] for _ in range(3)]

    for row in range(3):
        for col in range(3):
            buttons[row][col].config(text=" ")

# Sukuriame mygtukus
for row in range(3):
    for col in range(3):
        button = tk.Button(window, text=" ", font=('normal', 40), width=5, height=2,
                           command=lambda row=row, col=col: button_click(row, col))
        button.grid(row=row, column=col)
        buttons[row][col] = button

# Pradedame pagrindini cikla
window.mainloop()
