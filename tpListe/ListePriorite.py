class ListePriorite:
    def __init__(self):
        self.mainList = []
        self.min = None # on stocke le max et min qu'on update a chaque add pour ne pas parser la liste pour les trouver quand on les demande
        self.max = None

    @property
    def empty(self):
        return len(self.mainList) == 0

    @property
    def prio_min(self):
        return self.min

    @property
    def length(self):
        return len(self.mainList)

    @property
    def prio_max(self):
        return self.max

    def add(self , prio , obj):
        self.__update_max_and_min(prio)
        toAdd = (prio,obj)
        added = False
        for index in range(0,len(self.mainList)):
            if not added: # :/
                if self.mainList[index] > toAdd:
                    added = True
                    self.mainList.insert(index,(prio,obj))

        if not added:
            self.mainList.append(toAdd)

    def __update_max_and_min(self, prio):
        if self.min == None:
            self.min = prio
        if self.max == None:
            self.max = prio
        if self.max < prio:
            self.max = prio
        if self.min > prio:
            self.min = prio

    def __contains__(self, item):
        for tuple  in self.mainList:
            if item == tuple[1]:
                return True
        return False

    def contains (self,item):
        return self.__contains__(item)

    def priorities_of(self,obj):
        result = []
        for tuple in self.mainList:
            if obj == tuple[1]:
                result.append(tuple[0])
        return result

    def __str__(self):
        return self.mainList.__str__()

    def pop(self):
        return self.mainList.pop()

    def items(self):
        return self.mainList

    def vals(self):
        result = []
        for tuple in self.mainList:
            result.append(tuple[1])
        return result

    def at (self , index):
        return self.mainList[index]

    def delete (self , index):
        self.mainList.pop(index)

