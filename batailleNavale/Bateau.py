from Element import Element
class Bateau:
    def __init__(self,lig, col,isHorizontal,taille):
        self.elements = []
        self.status = 0
        self.nbTouche = 0
        for i in range (taille):
            if isHorizontal:
                self.elements.append(Element(lig, col+i))
            else:
                self.elements.append(Element(lig+i, col))


    def est_touche(self, lig , col):
        if self.status == 3:
            return 3
        for elmnt in self.elements:
            if elmnt.col == col and elmnt.lig == lig and not elmnt.estTouche : # le coup touche sur un element non deja touche
                self.nbTouche += 1
                if self.est_coule:
                    self.status = 3
                    return 3
                else:
                    return 2
            if elmnt.col == col and elmnt.lig == lig and elmnt.estTouche:  # le coup touche sur un element non deja touche
                return 1

        return 0

    @property
    def est_coule(self):
        return self.nbTouche == len(self.elements)



class Croiseur(Bateau):
    def __init__(self , lig ,col, isHorizontal):
        Bateau.__init__(self,lig,col,isHorizontal,3)

    def __str__(self):
        return 'Croiseur'

class Escorteur(Bateau):
    def __init__(self , lig , col , isHorizontal):
        Bateau.__init__(self,lig,col,isHorizontal,2)

    def __str__(self):
        return 'Escorteur'

class SousMarin(Bateau):

    def __init__(self,lig,col,isHorizontal):
        Bateau.__init__(self,lig,col,isHorizontal,1) #pas besoin de demander a l'user vertical ou horizontal pour un bateua de 1
        self.estPlonge = False


    def __str__(self):
        return 'Sous-marin'

    def est_touche(self, lig , col):
        if self.estPlonge:
            return 0
        else:
            Bateau.est_touche(self,lig,col)
