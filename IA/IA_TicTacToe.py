# faire une Ia qui joue au tictactoe

import pyautogui
import sys
import random


class IA_tictactoe():

    def __init__(self):
        pass

    def launch(self):
        pass

    def receive_msg(self):
        pass

    def random_behavior(self):
        # tableau des possiblité de click qui enleve les possibilité deja testées
        possibilities = {0, 8}
        # prendre une possibilité au hasard
        selecteur = random.randint(0, 8)
        # on recupere la ou il faut cliquer
        while possibilities[selecteur] > 0 and selected == 0:
            button_to_click = possibilities[selecteur]
            selected = 1
        pyautogui.click(x=100 * button_to_click, y=100 * button_to_click)

        # c'est quoi un test unitaire ??

    def make_move(self):
        pass


if __name__ == "__main__":
    current_IA = IA_tictactoe()
    current_IA.launch()
