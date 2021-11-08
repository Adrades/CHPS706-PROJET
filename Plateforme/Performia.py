import os
import platform
import pickle
from sys import stderr
try:
    from Game import Game
except :
    from Plateforme.Game import Game

try :
    from ServerThread import ServerThread
except :
    from Plateforme.ServerThread import ServerThread


class Performia:
    def __init__(self):
        """
        Initialise les données du programme, en chargeant la sauvegarde si il y en a une.
        """

        self._game_id = 0  # à sauvegarder
        self._games = []
        self.load_state()

        self._command = {
            ("add", "add_game", "ag"): self.add_game,
            ("sup", "sup_game", "sg"): self.sup_game,
            ("list", "list_game", "lg"): self.list_game,
            ("addia", "add_ia", "aa"): self.add_ia,
            ("supia", "sup_ia", "sa"): self.sup_ia,
            ("listia", "list_ia", "la"): self.list_ia,
            ("launch_session", "launch", "start"): self.launch_session,
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
        """
        pass

    def add_game(self):
        """
        Fonction qui ajoute un programme à la liste des jeux
        """
        titre = self.safe_input("Saisissez un titre pour le jeu : ")
        ip = self.safe_input("Saisissez une IP pour le serveur de jeu : ")
        port = int(self.safe_input("Saisissez un port pour le jeu : ", int))

        self._games.append(
            Game(
                self._game_id,
                titre,
                ip,
                port
            )
        )
        self._game_id += 1

    def add_ia(self):
        """
        Fonction qui ajoute une ia à l'un des jeux de la liste
        """
        self.list_game()

        game = self.get_game_by_id(
            int(self.safe_input("Saisissez l'identifiant du jeu où vous voulez ajouter une IA: ")))
        titre = self.safe_input("Saisissez un titre pour l'ia : ")
        ip = self.safe_input("Saisissez une IP pour le serveur de jeu : ")
        port = int(self.safe_input("Saisissez un port pour le jeu : ", int))
        game.add_ia(titre, ip, port)

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

        game = self.get_game_by_id(
            int(self.safe_input("Saisissez l'identifiant du jeu dont vous voulez supprimer une IA: ")))

        if game:
            game.list_ia()
            id_ia = int(self.safe_input("Saisissez l'identifiant de l'IA que vous voulez supprimer: "))
            trouve = False
            i = 0
            max_i = len(game.intelligences_artificiellles)
            while i < max_i and not trouve:
                if game.intelligences_artificiellles == id_ia:
                    game.sup_ia(id_ia)
                    trouve = True
                i += 1

            if trouve:
                print(f"L'IA numéro {id_ia} du jeu {game.titre} a été supprimé.")
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
        game = self.get_game_by_id(
            int(self.safe_input("Saisissez l'identifiant du jeu dont vous voulez lister une IA: ")))
        if game:
            game.list_ia()
        else:
            print("Aucun jeu avec cet identifiant n'a été trouvé!")

    def get_data_games(self):
        """
        Renvoie les données à sauvegarder pour la liste de jeux
        :return:
        """
        # todo specify data method in _games
        return self._games

    def get_game_by_id(self, id_game):
        """
        Renvoie un jeu de la liste
        :param id_game: L'ID du jeu en question
        :return: Retourne un jeu de la liste, ou None
        """
        i = 0
        max_i = len(self._games)
        while i < max_i:
            if self._games[i].identifiant == id_game:
                return self._games[i]
            i += 1
        return None

    @staticmethod
    def get_data_path():
        data_path = "."

        if platform.system().lower() == 'linux':
            app_data_path = os.path.expanduser("~")
            if not os.path.exists(f"{app_data_path}/.performia"):
                os.mkdir(f"{app_data_path}/.performia")
            data_path = f"{app_data_path}/.performia"

        elif platform.system().lower() == 'windows':
            app_data_path = os.getenv("APPDATA")
            if not os.path.exists(f"{app_data_path}\\Performia"):
                os.mkdir(f"{app_data_path}\\Performia")
            data_path = f"{app_data_path}\\Performia"

        else:
            print("La plateforme n'est pas reconnue", file=stderr)

        return data_path

    def save_state(self):
        data_path = self.get_data_path()
        data = {"_game_id": self._game_id, "_games": self._games}
        with open(f"{data_path}\\save_performia", 'wb') as outp:
            pickle.dump(data, outp)

    def load_state(self):
        data_path = self.get_data_path()
        if os.path.exists(f"{data_path}\\save_performia"):
            with open(f"{data_path}\\save_performia", 'rb') as inp:
                data = pickle.load(inp)
            self._game_id = data["_game_id"]
            self._games = data["_games"]

    def safe_input(self, prompt="", type_validation: type = str):
        """
        Fonction permettant de remplacer la fonction input, lorsque performia fonctionne en mode tty
        :param type_validation: Une fonction qui vérifie l'entrée
        :param prompt: Le message de demande d'entrée clavier de l'utilisateur
        :return: L'entrée de l'utilisateur
        """
        input_valide = False
        i = ""
        while not input_valide:
            i = input(prompt)
            try:
                type_validation(i)
                if i.lower() in self._reserved_command.keys():
                    pass
                    # todo choix selon la commande réservée
                else:
                    input_valide = True
            except ValueError:
                print(f"Mauvais type de données, essayer d'entrer un {type_validation.__doc__}")
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
        self.save_state()
        self.quitting = True
        print("Fin du programme")

    # def launch_session(self):
    #     ip, port = self._games[0].intelligences_artificiellles[0].ip, self._games[0].intelligences_artificiellles[
    #         0].port
    #     bytes_to_send = str.encode("Salut")
    #     # Create a UDP socket at client side
    #     sok = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    #     # Send to server using created UDP socket
    #     sok.sendto(bytes_to_send, (ip, port))

    def launch_session(self):
        """
        Kel : Launching the Performia session
        Consists of loading a game and its IA
        """
        game = self.get_game_by_id(
            int(self.safe_input("Saisissez l'identifiant du jeu que vous voulez lancer: ")))

        if game:
            # Todo lance uniquement la première IA de la liste, à améliorer
            thread_game = ServerThread(game.ip, self._games[0].port)
            thread_ia = ServerThread(game.intelligences_artificiellles[0].ip, game.intelligences_artificiellles[0].port)
            thread_game.start()
            thread_ia.start()
            print("Session Launched !")


if __name__ == '__main__':
    performia = Performia()
    performia()
