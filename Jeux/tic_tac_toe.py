import os
import socket
from tkinter import *
from tkinter import messagebox

from functools import partial

BOARD_SIZE_ROW = 3
BOARD_SIZE_GLOBAL = BOARD_SIZE_ROW * BOARD_SIZE_ROW
ICON_PATH = './icon/tictac.png'
global gagnant


class tictactoe():

    window = None
    playerTurn = True  # X = True  O = false
    count = 0
    board = []

    def __init__(self):
        self.loadWindow()
        self.loadBoard()
        self.bufferSize = 2048
        self.start_IA_comm()

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
        
        
        joueur = "X"
        if self.board[id]["text"] == "":
            self.board[id]["text"] = joueur
            self.checkifwin(joueur)
            self.count += 1
            self.playerTurn = not self.playerTurn
            
            #on passe au tour de l'ia
            self.send_IA()
            
            
            indice_joueia = self.recieve_IA()
            self.board[indice_joueia]["text"] = "O"
             
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
        
    def start_IA_comm(self):
        self.GameSocketInit = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        # il faut vérifier qu'il n'y a pas d'erreur ??

    def end_IA_comm(self):
        self.GameSocketInit.close()
        # il n'y a pas autre chsoe a faire ??
        #envoyer a l'ia que la communication est terminée
        
    def IA_error(self):
        pass
    
    def send_IA(self):
        Input_msg = ""
        
        for i in range(BOARD_SIZE_GLOBAL):
            if self.board[i]["text"] == "":
                Input_msg += (str(i) + "_") 
        bytesToSend = str.encode(Input_msg)

        serverAddressPort = ("127.0.0.1", 8081)
        #send Ia mais enfait on envoie au serveur pour q'uil envoie a l'ia connectée
        self.GameSocketInit.sendto(bytesToSend, serverAddressPort)
        
    def recieve_IA(self):
        IA_recived_move = self.GameSocketInit.recv(2048)
        
        indice_move = int(IA_recived_move[0].decode('utf-8'))
        #return un indice du coup joué par l'ia
        return indice_move
        

if __name__ == "__main__":
    currentGame = tictactoe()
    currentGame.launch()