class IA:
    def __init__(self, identifiant=0, titre="", chemin_executable=""):
        self.identifiant = identifiant
        self.titre = titre
        self.chemin_executable = chemin_executable
        self.score_IA = 0

    def __str__(self):
        return f"Identifiant\t:\t{self.identifiant}\nTitre\t:\t{self.titre}\nExecutable\t:\t{self.chemin_executable}\n"


if __name__ == '__main__':
    pass
