import pickle

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

    def each(self):
        for document in self.listDocument:
            yield document

    def sauve(self ,urlFic):
        with open(urlFic, 'wb') as f:
            pickle.dump(self.listDocument,f)

    def restore(self,urlFic):
        with open(urlFic, 'rb') as f:
            self.listDocument = pickle.load(f)