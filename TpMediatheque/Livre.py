from TpMediatheque.Text import Text

class Livre(Text):
    def __init__(self , editeur , annee):
        Text.__init__(self)
        self.editeur = editeur
        self.annee = annee

