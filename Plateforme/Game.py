class Game:
    """
    Classe permettant la gestion des jeux stockés par performia

    """

    def __init__(self, identifiant=0, titre="", chemin_executable=""):
        self.identifiant = identifiant
        self.titre = titre
        self.chemin_executable = chemin_executable


if __name__ == '__main__':
    game_test = Game()
