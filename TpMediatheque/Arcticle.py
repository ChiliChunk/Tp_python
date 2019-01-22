from TpMediatheque import Text

class Arcticle(Text):

    def __init__(self,titreRevue ,editeur , numEdition):
        self.titreRevue = titreRevue
        self.editeur = editeur
        self.numEdition = numEdition