class Mediatheque:

    def __init__(self):
        self.listDocument = []

    def add (self , oneDoc):
        self.listDocument.append(oneDoc)

    def __iadd__(self, oneDoc):
        self.add(oneDoc)
        return self

    def __delitem__(self, key):
        self.remove(key)

    def remove(self,key):
        self.listDocument.pop(key)
