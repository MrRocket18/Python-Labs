import tkinter as tk
import tkinter.messagebox as messagebox
from tkinter import simpledialog

def check_win(player):
    for i in range(3):
        if all(buttons[i * 3 + j]["text"] == player for j in range(3)):
            return True
        if all(buttons[i + j * 3]["text"] == player for j in range(3)):
            return True
    if all(buttons[i]["text"] == player for i in [0, 4, 8]):
        return True
    if all(buttons[i]["text"] == player for i in [2, 4, 6]):
        return True
    return False

def check_draw():
    return all(button["text"] != "" for button in buttons)

def button_click(row, col):
    global current_player
    index = row * 3 + col
    if buttons[index]["text"] == "":
        buttons[index]["text"] = current_player
        if check_win(current_player):
            messagebox.showinfo("Победа!", f"Игрок {current_player} победил!")
            disable_buttons()
            game_over()
        elif check_draw():
            messagebox.showinfo("Ничья!", "Ничья!")
            disable_buttons()
            game_over()
        else:
            current_player = "O" if current_player == "X" else "X"
            label.config(text=f"Ход игрока: {current_player}")
            if current_player == bot_player:
                bot_move()
                current_player = player_choice
                label.config(text=f"Ход игрока: {current_player}")

def disable_buttons():
    for button in buttons:
        button.config(state=tk.DISABLED)

def bot_move():
    best_score = -float('inf')
    best_move = None
    for i in range(9):
        if buttons[i]["text"] == "":
            buttons[i]["text"] = bot_player
            score = alphabeta(buttons, 0, -float('inf'), float('inf'), False)
            buttons[i]["text"] = ""
            if score > best_score:
                best_score = score
                best_move = i
    buttons[best_move]["text"] = bot_player
    if check_win(bot_player):
        messagebox.showinfo("Победа!", f"Бот ({bot_player}) победил!")
        disable_buttons()
        game_over()
    elif check_draw():
        messagebox.showinfo("Ничья!", "Ничья!")
        disable_buttons()
        game_over()

def alphabeta(board, depth, alpha, beta, maximizing_player):
    if check_win(bot_player):
        return 10
    if check_win(player_choice):
        return -10
    if check_draw():
        return 0

    if maximizing_player:
        max_eval = -float('inf')
        for i in range(9):
            if board[i]["text"] == "":
                board[i]["text"] = bot_player
                eval = alphabeta(board, depth + 1, alpha, beta, False)
                board[i]["text"] = ""
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if alpha >= beta:
                    return beta
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(9):
            if board[i]["text"] == "":
                board[i]["text"] = "X" if bot_player == "O" else "O"
                eval = alphabeta(board, depth + 1, alpha, beta, True)
                board[i]["text"] = ""
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if alpha >= beta:
                    return alpha
        return min_eval
def game_over():
    result = messagebox.askyesno("Игра окончена", "Хотите сыграть ещё раз?")
    if result:
        get_player_choice()
    else:
        root.destroy()


def start_new_game():
    global current_player, bot_player, buttons
    for button in buttons:
        button['text'] = ""
        button.config(state=tk.NORMAL)
    bot_player = "O" if player_choice == "X" else "X"  

    if player_choice == "O":
        current_player = bot_player 
        bot_move()
        current_player = player_choice
        label.config(text=f"Ход игрока: O")

    else:
        current_player = "X" 
        label.config(text=f"Ход игрока: X")


def get_player_choice():
    global player_choice, current_player
    root.withdraw()
    player_choice = simpledialog.askstring("Выбор игрока", "Выберите, чем хотите играть (X или O):", initialvalue="X").upper()
    if player_choice not in ("X", "O"):
        messagebox.showerror("Ошибка", "Неверный ввод. Пожалуйста, введите X или O.")
        get_player_choice()
    root.deiconify()
    start_new_game()

root = tk.Tk()
root.title("Крестики-нолики")
buttons = []
bot_player = "O"

label = tk.Label(root, text=f"Ход игрока: ", font=("Helvetica", 16))
label.grid(row=0, column=0, columnspan=3, pady=10)

for i in range(3):
    for j in range(3):
        button = tk.Button(root, text="", width=10, height=5, font=("Helvetica", 32), command=lambda row=i, col=j: button_click(row, col))
        button.grid(row=i + 1, column=j, padx=5, pady=5)
        buttons.append(button)

get_player_choice()

root.mainloop()