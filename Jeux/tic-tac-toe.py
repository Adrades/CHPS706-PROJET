import os
from tkinter import *
from tkinter import messagebox

from functools import partial

BOARD_SIZE_ROW = 3
BOARD_SIZE_GLOBAL = BOARD_SIZE_ROW * BOARD_SIZE_ROW
ICON_PATH = './icon/tictac.png'
global gagnant

class game():

    window = None
    playerTurn = True # X = True  O = false
    count = 0
    board = []

    def __init__(self):
        self.loadWindow()
        self.loadBoard()

    def loadBoard(self):
        # faire des boutons cliquables
        for i in range(BOARD_SIZE_GLOBAL):
            self.board.append(
                Button(self.window,
                    text="",
                    font=("Helvetica", 20),
                    height=3,
                    width=6,
                    bg="SystemButtonFace",
                    command=partial(self.b_click, i)
                )
            )

        for i in range(BOARD_SIZE_GLOBAL):
            self.board[i].grid(row=i%BOARD_SIZE_ROW, column=int(i/BOARD_SIZE_ROW))

    def loadWindow(self):
        self.window = Tk()
        self.window.title('Tic-Tac-Toe')
        # root.iconbitmap("c:/Users/lougo/Desktop/cours/master 1/CHPS706-PROJET/Jeux/icon/tictac2.ico")
        # root.iconbitmap('./icon/tictac2.ico')
        if os.path.isfile(ICON_PATH):
            self.window.iconphoto(False, PhotoImage(file=ICON_PATH))

    def checkifwin(self, joueur):  # joueur est soit "X" soit "O" rien d'autre
        global gagnant
        retry = False
        gagnant = False

        # horizontal
        for i in range(BOARD_SIZE_ROW):
            for j in range(BOARD_SIZE_ROW):
                if (self.board[i+j*BOARD_SIZE_ROW]["text"] != joueur):
                    break
                if j == BOARD_SIZE_ROW - 1:
                    gagnant = True
                    break
            if gagnant:
                break

        # Vertical
        for i in range(BOARD_SIZE_ROW):
            for j in range(BOARD_SIZE_ROW):
                if (self.board[i*BOARD_SIZE_ROW+j]["text"] != joueur):
                    break
                if j == BOARD_SIZE_ROW - 1:
                    gagnant = True
                    break
            if gagnant:
                break

        # Diag 1
        for i in range(BOARD_SIZE_ROW):
            if (self.board[i*BOARD_SIZE_ROW+i]["text"] != joueur):
                break
            if i == BOARD_SIZE_ROW - 1:
                gagnant = True
                break

        # Diag 2
        for i in range(BOARD_SIZE_ROW):
            if (self.board[BOARD_SIZE_ROW - 1 + i * (BOARD_SIZE_ROW -1)]["text"] != joueur):
                break
            if i == BOARD_SIZE_ROW - 1:
                gagnant = True
                break

        if gagnant is True:
            retry = messagebox.askyesno("Victoire", joueur + " a gagné\n\nvoulez-vous recommencer ?")
        if retry is True:
            for i in range(BOARD_SIZE_GLOBAL):
                self.board[i]["text"] = ""
        elif gagnant is True:
            self.window.destroy()  # fermer le jeu

    # actions de boutons
    def b_click(self, id):

        joueur = "X" if self.playerTurn else "O"
        if self.board[id]["text"] == "":
            self.board[id]["text"] = joueur
            self.playerTurn = not self.playerTurn
            self.count += 1
            self.checkifwin(joueur)
        else:
            messagebox.showerror("TicTac", "Cette case a déjà été sélectionnée")

    def launch(self):
        self.window.mainloop()

if __name__ == "__main__":
    currentGame = game()
    currentGame.launch()