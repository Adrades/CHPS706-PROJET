from unittest import TestCase
from random import randint
from Plateforme.Performia import Performia

from sys import stdin


def gen_string():
    return str([int(randint(65, 90)) for _ in range(randint(0, 100))])


class TestPerformia(TestCase):
    # def __init__(self):
    #     Performia.__init__(self)
    #     print("q", file=stdin)

    def test_add_sup_game(self):
        """Teste l'ajout et la suppression de jeux"""
        random_name = gen_string()
        random_path = gen_string()
        p = Performia(test=True)
        p.add_game()
        print(random_name, random_path, sep="\n", file=stdin)
        self.assertEqual(p._games[-1].identifiant, p._game_id - 1)
        self.assertEqual(p._games[-1].titre, random_name)
        self.assertEqual(p._games[-1].chemin_executable, random_path)
        p.sup_game()
        print(-1, file=stdin)
        p.sup_game()
        print(p._game_id - 1)
        if len(p._games) > 0:
            self.assertNotEqual(p._games[-1].identifiant, p._game_id - 1)
        self.assertEqual(p._removed_games[-1].identifiant, p._game_id - 1)
        p._game_id -= 1
        p.quit()

    def test_add_ia(self):
        self.fail()

    def test_sup_ia(self):
        self.fail()

    def test_list_game(self):
        self.fail()

    def test_list_ia(self):
        self.fail()

    def test_get_data_games(self):
        self.fail()

    def test_get_data_path(self):
        self.fail()

    def test_save_state(self):
        self.fail()

    def test_load_state(self):
        self.fail()

    def test_safe_input(self):
        self.fail()

    def test_help(self):
        self.fail()

    def test_quit(self):
        self.fail()
