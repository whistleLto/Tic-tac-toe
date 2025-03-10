from tkinter import *
import random

win = Tk()
win.title("TicTacToe")
win.resizable(False, False)

turn = True  

def check_winner():
    # Check rows
    for row in range(3):
        if buttons[row][0]["text"] == buttons[row][1]["text"] == buttons[row][2]["text"] != "":
            return buttons[row][0]["text"]

    # Check columns
    for col in range(3):
        if buttons[0][col]["text"] == buttons[1][col]["text"] == buttons[2][col]["text"] != "":
            return buttons[0][col]["text"]

    # Check diagonals
    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        return buttons[0][0]["text"]
    if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        return buttons[0][2]["text"]

    # Check for tie
    if all(buttons[r][c]["text"] != "" for r in range(3) for c in range(3)):
        return "Tie"

    return None  

def end_game(winner):
    if winner == "Tie":
        result_lbl.config(text="Tie!")
        win.title("TicTacToe - It's a Tie!")
    else:
        result_lbl.config(text=f"{winner} won!") 
        win.title(f"TicTacToe - {winner} Wins!")

    for row in buttons:
        for button in row:
            button.config(state=DISABLED)

def player_turn(row, column):
    global turn
    if buttons[row][column]["text"] == "":
        buttons[row][column].config(text="X", state=DISABLED)
        turn = False

        winner = check_winner()
        if winner:
            end_game(winner)
            return  

        Ai()

def Ai():
    global turn
    empty_spaces = [(r, c) for r in range(3) for c in range(3) if buttons[r][c]["text"] == ""]

    # Check if AI can win
    for r, c in empty_spaces:
        buttons[r][c]["text"] = "O"
        if check_winner() == "O":
            buttons[r][c].config(state=DISABLED)
            end_game("O")
            return
        buttons[r][c]["text"] = ""  

    
    for r, c in empty_spaces:
        buttons[r][c]["text"] = "X"
        if check_winner() == "X":
            buttons[r][c].config(text="O", state=DISABLED)
            turn = True
            return
        buttons[r][c]["text"] = ""  

    
    if empty_spaces:
        row, column = random.choice(empty_spaces)
        buttons[row][column].config(text="O", state=DISABLED)

        winner = check_winner()
        if winner:
            end_game(winner)
        else:
            turn = True  

def reset():
    global turn
    turn = True 

    win.title("TicTacToe")  
    result_lbl.config(text="Tic-Tac-Toe")

    for row in range(3):
        for col in range(3):
            buttons[row][col].config(text="", state=NORMAL)

buttons = []

result_lbl = Label(win, font=('Arial', 16), text="Tic-Tac-Toe")
result_lbl.pack()

reset_button = Button(win, text="Reset", font=('Arial', 16), command=reset)
reset_button.pack(side="top")

frame = Frame(win)
frame.pack()

for i in range(3):
    row_buttons = []
    for j in range(3):
        button = Button(frame, text="", width=10, height=5, font=('Arial', 16),
                        command=lambda r=i, c=j: player_turn(r, c))
        button.grid(row=i, column=j)
        row_buttons.append(button)
    buttons.append(row_buttons)

win.mainloop()
