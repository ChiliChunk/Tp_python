from gestion_index import Entry

class index:
    def __init__(self):
        self.entries = {} #key : entry.title , value: entry

    def add (self, entry):
        self.entries[entry.title] = entry
        return self

    def __str__(self):
        result = ""
        currentLetter = None
        for key in  sorted(self.entries):
            testLetter =  key[0]
            if testLetter != currentLetter:
                currentLetter = testLetter
                result += currentLetter.upper() +"\n"
            temp = self.entries.get(key).__str__()
            result += temp

        return  result




if __name__ == '__main__':
    i = index()
    e = Entry('test')
    e.addNormalPage(7)
    e.addNormalPage(5)
    e.addPageDef(1)
    e.addPageDef(2)
    e2 = Entry("test22")
    e2.addPageDef(3)
    e2.addPageDef(5)
    e2.addNormalPage(8)
    e.addSubEntry(e2)
    e3 = Entry("osef")
    i.add(e)
    i.add(e3)
    print(i)