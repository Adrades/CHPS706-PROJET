#!/usr/bin/env python3

import os
import socket
from tkinter import *
from tkinter import messagebox

from functools import partial

BOARD_SIZE_ROW = 3
BOARD_SIZE_GLOBAL = BOARD_SIZE_ROW * BOARD_SIZE_ROW
ICON_PATH = './icon/tictac.png'
global tableau
global gagnant


class tictactoe():
    window = None
    playerTurn = True  # X = True  O = false
    count = 0
    board = []

    def __init__(self):
        self.load_window()
        self.load_board()
        self.bufferSize = 2048
        self.start_ia_comm()

    def load_board(self):
        # faire des boutons cliquables
        for i in range(BOARD_SIZE_GLOBAL):
            self.board.append(
                Button(self.window,
                       text="",
                       font=("Helvetica", 20),
                       height=3,
                       width=6,
                       bg="White",
                       command=partial(self.b_click, i)
                       )
            )

        for i in range(BOARD_SIZE_GLOBAL):
            self.board[i].grid(row=i % BOARD_SIZE_ROW, column=int(i / BOARD_SIZE_ROW))

    def load_window(self):
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
                if self.board[i + j * BOARD_SIZE_ROW]["text"] != joueur:
                    break
                if j == BOARD_SIZE_ROW - 1:
                    gagnant = True
                    break
            if gagnant:
                break

        # Vertical
        for i in range(BOARD_SIZE_ROW):
            for j in range(BOARD_SIZE_ROW):
                if self.board[i * BOARD_SIZE_ROW + j]["text"] != joueur:
                    break
                if j == BOARD_SIZE_ROW - 1:
                    gagnant = True
                    break
            if gagnant:
                break

        # Diag 1
        for i in range(BOARD_SIZE_ROW):
            if self.board[i * BOARD_SIZE_ROW + i]["text"] != joueur:
                break
            if i == BOARD_SIZE_ROW - 1:
                gagnant = True
                break

        # Diag 2
        for i in range(BOARD_SIZE_ROW):
            if self.board[BOARD_SIZE_ROW - 1 + i * (BOARD_SIZE_ROW - 1)]["text"] != joueur:
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

        joueur = "X"
        if self.board[id]["text"] == "":
            self.board[id]["text"] = joueur
            self.checkifwin(joueur)
            self.count += 1
            self.playerTurn = not self.playerTurn

            indice_joueia = id

            while self.board[int(indice_joueia)]["text"] != "":
                self.send_ia()

                indice_joueia = self.GameSocketInit.recv(2048)

            self.board[int(indice_joueia)]["text"] = "O"

            self.checkifwin("O")
            self.count += 1
            self.playerTurn = not self.playerTurn

        else:
            self.send_error()

    def launch(self):
        self.window.mainloop()

    def send_error(self):
        # envoyer une erreur a l'ia
        messagebox.showerror("TicTacToe", "Cette case a déjà été sélectionnée")

    def start_ia_comm(self):
        self.GameSocketInit = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        # il faut vérifier qu'il n'y a pas d'erreur ??

    def end_ia_comm(self):
        self.GameSocketInit.close()
        # il n'y a pas autre chsoe a faire ??
        # envoyer a l'ia que la communication est terminée

    def ia_error(self):
        pass

    def send_ia(self):
        input_msg = ""

        for i in range(BOARD_SIZE_GLOBAL):
            if self.board[i]["text"] == "":
                input_msg += (str(i) + "_")
        bytes_to_send = str.encode(input_msg)

        server_address_port = ("127.0.0.1", 8081)
        # send Ia mais enfait on envoie au serveur pour q'uil envoie a l'ia connectée
        self.GameSocketInit.sendto(bytes_to_send, server_address_port)


if __name__ == "__main__":
    currentGame = tictactoe()
    currentGame.launch()
