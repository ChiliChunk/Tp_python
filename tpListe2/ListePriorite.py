"""Permet de creer une liste avec des priorites"""

class ListePriorite:
    def __init__(self):
        self.mainList = []
        self.min = None # on stocke le max et min qu'on update a chaque add pour ne pas parser la liste pour les trouver quand on les demande
        self.max = None

    @property
    def empty(self):
        """Permet de savoir si la liste est vide"""
        return len(self.mainList) == 0

    @property
    def prio_min(self):
        """Renvoie la priorité minimum presente dans la liste"""
        return self.min

    @property
    def length(self):
        """Renvoie la taille de la liste"""
        return len(self.mainList)

    @property
    def prio_max(self):
        """Renvoie la priorité maximale presente dans la liste"""
        return self.max

    def add(self , prio , obj):
        """Ajout un objet obj a la liste avec la priorité prio"""
        self.__update_max_and_min(prio)
        toAdd = (prio,obj)
        added = False
        for index in range(0, len(self.mainList)):
            if not added: # :/
                if self.mainList[index] > toAdd:
                    added = True
                    self.mainList.insert(index,(prio,obj))

        if not added:
            self.mainList.append(toAdd)

    def __iadd__(self, tuple):
        """Same as add"""
        self.add(tuple[0], tuple[1])
        return self

    def __update_max_and_min(self, prio):
        """permet de mettre a jour les variable min et max"""
        if self.min == None:
            self.min = prio
        if self.max == None:
            self.max = prio
        if self.max < prio:
            self.max = prio
        if self.min > prio:
            self.min = prio

    def __contains__(self, item):
        """Permet de savoir si l'item item est present dans la liste"""
        for tuple  in self.mainList:
            if item == tuple[1]:
                return True
        return False

    def contains (self,item):
        """same as __contains__"""
        return self.__contains__(item)

    def priorities_of(self,obj):
        """Permet de connaitre la priorité d'un obj de la liste"""
        result = []
        for tuple in self.mainList:
            if obj == tuple[1]:
                result.append(tuple[0])
        return result

    def __str__(self):
        """Renvoie le contenu de la liste sous forme de string"""
        return self.mainList.__str__()

    def pop(self):
        """Supprime et retourne le dernier element de la liste"""
        return self.mainList.pop()

    def items(self):
        """Renvoie le contenu de la liste"""
        return self.mainList

    def vals(self):
        """Renvoie les valeurs(sans la priorité) des elements dans la liste"""
        result = []
        for tuple in self.mainList:
            result.append(tuple[1])
        return result

    def at (self , index):
        """Renvoie la valeur a l'indice presisé"""
        return self.mainList[index]

    def delete (self , index):
        """Supprime la valeur a l'indice precisé"""
        self.mainList.pop(index)

    def __delitem__(self, key):
        self.mainList.pop(key)

