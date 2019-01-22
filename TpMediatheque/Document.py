class Document:

    # def __init__(self, auteur,titre,copyright=None):
    #     self.auteur = auteur
    #     self.titre = titre
    #     if copyright != None:
    #         self.copyright = copyright

    def __init__(self):
            ...

    def afficher(self):
        print(f"Affichage du doc {self.titre}")