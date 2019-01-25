import Bateau
class Grille():

    def __init__(self , nbLignes , nbCol):
        self.mainList = []
        self.nbLignes = nbLignes
        self.nbCol= nbCol

    def __str__(self):
        result = ""
        for bateau in self.mainList:
            if not bateau.est_coule:
                result += bateau.__str__()
                result += " "
        return result


    @property
    def nb_lig_max(self):
        return self.nbLignes

    @property
    def nb_col_max(self):
        return self.nbCol

    def __iadd__(self, other):
        self.mainList.append(other)
        return self

    def coup(self,lig,col):
        if lig > self.nb_lig_max or col > self.nb_col_max or lig < 0 or col < 0:
            return -1

        else:
            for bateau in self.mainList:
                test = bateau.est_touche(lig,col)
                if  test != 0:
                    return test
        return 0