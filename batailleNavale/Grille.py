import Bateau
class Grille():

    def __init__(self , nbLignes , nbCol):
        self.mainList = []
        self.nbLignes = nbLignes
        self.nbCol= nbCol

    def __str__(self):
        return  f"{' '.join(str(e) for e in self.mainList)} "


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
                if bateau.est_touche(lig,col) != 0:
                    return bateau.est_touche(lig,col)
        return 0

if __name__ == '__main__':
    s = Bateau.SousMarin(2,3,True)
    g = Grille(4,4)
    g += s
    g += Bateau.SousMarin(1,3,False)
    print(g)