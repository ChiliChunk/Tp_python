class Element:
    def __init__(self ,lig , col):
        self.lig = lig
        self.col = col
        self.aEteTouche = False

    @property
    def estTouche(self):
        return self.aEteTouche

    def __str__(self):
        return 'X' if self.estTouche else ''

    def toucher(self):
        self.aEteTouche = True