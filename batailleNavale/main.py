from Grille import Grille
import Bateau

b1 = Bateau.Croiseur(1, 1, True)
b2 = Bateau.Escorteur(2, 5, False)
b3 = Bateau.SousMarin(4, 2, False)

g1 = Grille(7, 9)

g1 += b1
g1 += b2
g1 += b3
print(b1.est_touche(1, 1))
print(b1.est_touche(1, 2))
print(b1.est_touche(1, 2))
print(b1.est_touche(1, 3))
print(g1.coup(1, 4))