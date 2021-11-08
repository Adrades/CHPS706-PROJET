from IA import IA


class Game:
    """
    Classe permettant la gestion des jeux stockés par performia

    """

    def __init__(self, identifiant=0, titre="", ip="127.0.0.1", port=25565):
        self.identifiant = identifiant
        self.titre = titre
        self.ip = ip
        self.port = port

        self.intelligences_artificiellles = []
        self.id_ia = 0
        self.backup_ia = []

    def add_ia(self, titre="", ip="127.0.0.1", port=8080):
        """
        Méthode qui ajoute une IA à la liste de celles gérées par un certain jeu.
        :param titre: Le nom d'une IA
        :param ip: Ip du serveur l'IA
        :param port: port où tourne l'AI
        """
        # todo ajouter la gestion des paramètres du lancement d'une IA, voir avec l'équipe jeux.
        # todo ajouter la vérification du chemin

        self.intelligences_artificiellles.append(IA(self.id_ia, titre, ip, port))
        self.id_ia += 1

    def sup_ia(self, identifiant):
        """
        Méthode qui retire une IA de la liste des IAs acceptées par le jeu.
        :param identifiant:
        :return:
        """
        self.backup_ia.append(
            self.intelligences_artificiellles.pop(
                self.intelligences_artificiellles.index(
                    list(filter(lambda a: a.identifiant == identifiant, self.intelligences_artificiellles))[0]
                )
            )
        )

    def list_ia(self):
        for ia in self.intelligences_artificiellles:
            print(ia)

    def __str__(self):
        return f"Identifiant\t:\t{self.identifiant}\nTitre\t:\t{self.titre}\nExecutable\t:\t{self.ip}:{self.port}\n"


if __name__ == '__main__':
    game_test = Game()
    game_test.add_ia("IA_zero", "179.0.0.4")
    game_test.add_ia("IA_un", "179.0.0.8")
    game_test.add_ia("IA_deux")
    game_test.add_ia("IA_trois", "179.0.0.1", 1545)
    game_test.sup_ia(0)
    print(*[str(ia) for ia in game_test.intelligences_artificiellles])
