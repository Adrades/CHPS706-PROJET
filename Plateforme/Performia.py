from sys import stderr
from Game import Game


class Performia:
    def __init__(self):
        # todo gérer la récupération d'un potentiel état du jeu sauvegardé

        """
        Format d'un jeu:
            - id
            - titre
            -
        """
        self._game_id = 0  # à sauvegarder
        self._games = []
        self._command = {
            ("add", "add_game", "ag"): self.add_game,
            ("sup", "sup_game", "sg"): self.sup_game,
            ("list", "list_game", "lg"): self.list_game,
            ("q", "quit"): self.quit,
        }

        self._reserved_command = {
            ("q", "quit"): self.quit
        }
        self._removed_games = []
        self.quitting = False

    def add_game(self):
        """
        Fonction qui ajoute un programme à la liste des jeux
        :return:
        """
        titre = self.safe_input("Saisissez un titre pour le jeu : ")
        chemin = self.safe_input(f"Saisissez le chemin de l'executable du jeu : ")
        self._games.append(
            Game(
                self._game_id,
                titre,
                chemin
            )
        )
        self._game_id += 1

    def sup_game(self):
        """
        Fonction qui supprime un jeu
        :return:
        """
        self.list_game()

        iden = int(self.safe_input("Saisissez l'identifiant du jeu que vous voulez supprimer : "))

        trouve = False
        i = 0
        max_i = len(self._games)

        while i < max_i and not trouve:
            if self._games[i].identifiant == iden:
                self._removed_games.append(self._games.pop(i))
                trouve = True

        if trouve:
            print(f"Le jeu {self._removed_games[-1].titre} ({self._removed_games[-1].identifiant}) a été supprimé.")
        else:
            print("Aucun jeu avec cet identifiant n'a été trouvé!")

    def list_game(self):
        """
        Fonction qui liste les jeux géré par performia
        :return:
        """
        for g in self._games:
            print(
                f"Identifiant\t:\t{g.identifiant}\n"
                f"Titre\t:\t{g.titre}\n"
                f"Executable\t:\t{g.chemin_executable}\n"
            )

    def safe_input(self, prompt=""):
        """
        Fonction permettant de remplacer la fonction input, lorsque performia fonctionne en mode tty
        :param prompt:
        :return:
        """
        input_valide = False
        i = ""
        while not input_valide:
            i = input(prompt)

            # todo ajouter une vérification regex de l'input ?
            if i.lower() in self._reserved_command.keys():
                pass
                # todo choix selon la commande réservée
            else:
                input_valide = True

        return i

    def quit(self):
        # todo faire ce qu'il faut pour que l'application quitte
        self.quitting = True

    def __call__(self, *args, **kwargs):
        """
        La boucle principale
        :param args:
        :param kwargs:
        :return:
        """

        print("Démarrage de perfomia")

        while not self.quitting:
            i = self.safe_input("> ")
            for j in range(len(list(self._command.keys()))):
                if i in list(self._command.keys())[j]:
                    self._command[list(self._command.keys())[j]]()

    def __del__(self):
        """
        Enregistre l'état du programme
        :return:
        """
        # todo enregistrer l'état du programme à la fin


if __name__ == '__main__':
    performia = Performia()
    performia()
