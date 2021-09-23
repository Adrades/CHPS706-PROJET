from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Tic-Tac-Toe')
# root.iconbitmap("c:/Users/lougo/Desktop/cours/master 1/CHPS706-PROJET/Jeux/icon/tictac2.ico")
# root.iconbitmap('./icon/tictac2.ico')
root.iconphoto(False, PhotoImage(file='./icon/tictac.png'))

# X = True  O = false
clicked = True
count = 0
global gagnant


def checkifwin(joueur):  # joueur est soit "X" soit "O" rien d'autre
    global gagnant
    retry = False
    gagnant = False

    if b1["text"] == joueur and b2["text"] == joueur and b3["text"] == joueur:  # que des X sur la premiere ligne
        gagnant = True
    if b1["text"] == joueur and b4["text"] == joueur and b7["text"] == joueur:  # que des X sur la premiere colonne
        gagnant = True
    if b1["text"] == joueur and b5["text"] == joueur and b9["text"] == joueur:
        # que des X sur la diagonale hautgauche/basdroit
        gagnant = True
    if b2["text"] == joueur and b6["text"] == joueur and b8["text"] == joueur:  # que des X sur la deuxième colonne
        gagnant = True
    if b4["text"] == joueur and b5["text"] == joueur and b6["text"] == joueur:  # que des X sur la deuxième ligne
        gagnant = True
    if b3["text"] == joueur and b5["text"] == joueur and b7["text"] == joueur:
        # que des X sur la diagonale hautdroite/basgauche
        gagnant = True
    if b7["text"] == joueur and b8["text"] == joueur and b9["text"] == joueur:  # que des X sur la troisième ligne
        gagnant = True
    if b3["text"] == joueur and b6["text"] == joueur and b9["text"] == joueur:  # que des X sur la troisième colonne
        gagnant = True
    if gagnant is True:
        retry = messagebox.askyesno("Victoire", joueur + " a gagné\n\nvoulez-vous recommencer ?")
    if retry is True:
        b1["text"] = ""  # recommencer la partie tout mettre a ""
        b2["text"] = ""
        b3["text"] = ""
        b4["text"] = ""
        b5["text"] = ""
        b6["text"] = ""
        b7["text"] = ""
        b8["text"] = ""
        b9["text"] = ""
    elif gagnant is True:
        root.destroy()  # fermer le jeu


# actions de boutons
def b_click(b):
    global clicked, count
    joueur = "X"
    if b["text"] == "" and clicked is True:
        b["text"] = "X"
        clicked = False
        joueur = "X"
        count += 1
    elif b["text"] == "" and clicked is False:
        b["text"] = "O"
        clicked = True
        count += 1
        joueur = "O"
    else:
        messagebox.showerror("TicTac", "Cette case a déjà été sélectionnée")
    checkifwin(joueur)


# faire des boutons cliquables
b1 = Button(root, text="", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
            command=lambda: b_click(b1))
b2 = Button(root, text="", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
            command=lambda: b_click(b2))
b3 = Button(root, text="", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
            command=lambda: b_click(b3))

b4 = Button(root, text="", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
            command=lambda: b_click(b4))
b5 = Button(root, text="", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
            command=lambda: b_click(b5))
b6 = Button(root, text="", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
            command=lambda: b_click(b6))

b7 = Button(root, text="", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
            command=lambda: b_click(b7))
b8 = Button(root, text="", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
            command=lambda: b_click(b8))
b9 = Button(root, text="", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
            command=lambda: b_click(b9))

b1.grid(row=0, column=0)
b2.grid(row=0, column=1)
b3.grid(row=0, column=2)

b4.grid(row=1, column=0)
b5.grid(row=1, column=1)
b6.grid(row=1, column=2)

b7.grid(row=2, column=0)
b8.grid(row=2, column=1)
b9.grid(row=2, column=2)
value = 0
value += 1
# messagebox.askokcancel("debut", "test " + value.__str__())
value += 1
root.mainloop()
