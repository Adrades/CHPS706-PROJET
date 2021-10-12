from sys import stderr
from Game import Game


class Performia:
    def __init__(self):
        # todo gérer la récupération d'un potentiel état du jeu sauvegardé

        self._game_id = 0  # à sauvegarder
        self._games = []
        self._command = {
            ("add", "add_game", "ag"): self.add_game,
            ("sup", "sup_game", "sg"): self.sup_game,
            ("list", "list_game", "lg"): self.list_game,
            ("addia", "add_ia", "aa"): self.add_ia,
            ("supia", "sup_ia", "sa"): self.sup_ia,
            ("listia", "list_ia", "la"): self.list_ia,
            ("q", "quit"): self.quit,
            ("h", "help"): self.help,
        }

        self._reserved_command = {
            ("q", "quit"): self.quit
        }
        self._removed_games = []
        self.quitting = False

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

    def add_game(self):
        """
        Fonction qui ajoute un programme à la liste des jeux
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

    def add_ia(self):
        """
        Fonction qui ajoute une ia à l'un des jeux de la liste
        """
        self.list_game()

        n_game = int(self.safe_input("Saisissez l'identifiant du jeu auquel vous voulez ajouter une IA : "))
        titre = self.safe_input("Saisissez un titre pour l'ia : ")
        chemin = self.safe_input(f"Saisissez le chemin de l'executable de l'ia : ")
        self._games[n_game].add_ia(titre, chemin)

    def sup_game(self):
        """
        Fonction qui supprime un jeu
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
            i += 1

        if trouve:
            print(f"Le jeu {self._removed_games[-1].titre} ({self._removed_games[-1].identifiant}) a été supprimé.")
        else:
            print("Aucun jeu avec cet identifiant n'a été trouvé!")

    def sup_ia(self):
        """
        Fonction qui supprime l'ia d'un jeu
        """
        self.list_game()

        id_game = int(self.safe_input("Saisissez l'identifiant du jeu dont vous voulez supprimer une IA: "))
        id_ia = 0
        found_game: Game

        trouve = False
        i = 0
        max_i = len(self._games)
        while i < max_i and not trouve:
            if self._games[i].identifiant == id_game:
                found_game = self._games[i]
                trouve = True
            i += 1

        if trouve:
            found_game.list_ia()
            id_ia = int(self.safe_input("Saisissez l'identifiant de l'IA que vous voulez supprimer: "))
            trouve = False
            i = 0
            max_i = len(found_game.intelligences_artificiellles)
            while i < max_i and not trouve:
                if found_game.intelligences_artificiellles == id_ia:
                    found_game.sup_ia(id_ia)
                    trouve = True
                i += 1

            if trouve:
                print(f"L'IA numéro {id_ia} du jeu {found_game.titre} a été supprimé.")
            else:
                print("Aucune IA avec cet identifiant n'a été trouvée!")
        else:
            print("Aucun jeu avec cet identifiant n'a été trouvé!")

    def list_game(self):
        """
        Fonction qui liste les jeux géré par performia
        """
        for g in self._games:
            print(g)

    def list_ia(self):
        """
        Fonction qui liste les IAs d'un jeu
        """
        self.list_game()

        id_game = int(self.safe_input("Saisissez l'identifiant du jeu dont vous voulez consulter les IA: "))
        id_ia = 0
        found_game: Game

        trouve = False
        i = 0
        max_i = len(self._games)
        while i < max_i and not trouve:
            if self._games[i].identifiant == id_game:
                found_game = self._games[i]
                trouve = True
            i += 1

        if trouve:
            found_game.list_ia()
        else:
            print("Aucun jeu avec cet identifiant n'a été trouvé!")

    def safe_input(self, prompt=""):
        """
        Fonction permettant de remplacer la fonction input, lorsque performia fonctionne en mode tty
        :param prompt: Le message de demande d'entrée clavier de l'utilisateur
        :return: L'entrée de l'utilisateur
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

    def help(self):
        """
        Fonction qui affiche les commandes disponibles pour l'utilisateur
        """

        for j in range(len(list(self._command.keys()))):
            c = list(self._command.keys())[j]
            print(f"{c} : {self._command[list(self._command.keys())[j]].__doc__}")

    def quit(self):
        """
        Fonction qui éteint proprement le programme.
        """

        # Doit être complémentaire avec __del__ !!

        # todo faire ce qu'il faut pour que l'application quitte, __del__ est automatiquement appelé après
        self.quitting = True
        print("Fin du programme")


if __name__ == '__main__':
    performia = Performia()
    performia()
