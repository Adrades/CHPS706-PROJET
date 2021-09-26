from IA import IA


class Game:
    """
    Classe permettant la gestion des jeux stockés par performia

    """

    def __init__(self, identifiant=0, titre="", chemin_executable=""):
        self.identifiant = identifiant
        self.titre = titre
        self.chemin_executable = chemin_executable
        self.intelligences_artificiellles = []
        self.id_ia = 0

        self.backup_ia = []

    def add_ia(self, titre="", chemin_executable=""):
        """
        Méthode qui ajoute une IA à la liste de celles gérées par un certain jeu.
        :param titre: Le nom d'une IA
        :param chemin_executable: Le chemin de l'éxecutable d'une IA
        """
        # todo ajouter la gestion des paramètres du lancement d'une IA, voir avec l'équipe jeux.
        # todo ajouter la vérification du chemin

        self.intelligences_artificiellles.append(IA(self.id_ia, titre, chemin_executable))
        self.id_ia += 1

    def sup_ia(self, identifiant):
        self.backup_ia.append(
            self.intelligences_artificiellles.pop(
                self.intelligences_artificiellles.index(
                    list(filter(lambda a: a.identifiant == identifiant, self.intelligences_artificiellles))[0]
                )
            )
        )


if __name__ == '__main__':
    game_test = Game()
