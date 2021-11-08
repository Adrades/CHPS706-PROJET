class IA:
    def __init__(self, identifiant=0, titre="", ip="127.0.0.1", port=8001):
        self.identifiant = identifiant
        self.titre = titre
        self.score_IA = 0
        self.ip = ip
        self.port = port

    def __str__(self):
        return f"Identifiant\t:\t{self.identifiant}\nTitre\t:\t{self.titre}\nExecutable\t:\t{self.ip}:{self.port}\n"


if __name__ == '__main__':
    pass
