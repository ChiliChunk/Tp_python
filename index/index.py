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

    def addSubEntry(self , parentEntry , subEntry):
        if parentEntry in list(self.entries.keys()):
            self.entries.get(parentEntry).subEntry.add(Entry(subEntry))
        else:
            self.entries[parentEntry] = Entry(parentEntry)
            self.entries.get(parentEntry).subEntry.add(Entry(subEntry))


    def addPage(self , entryName , num , isDef , parentEntry=None):

        if parentEntry == None: # in lvl 1 entry
            if isDef:
                self.entries.get(entryName).defPage.add(num)
            else:
                self.entries.get(entryName).normalPage.add(num)

        else: # if parentEntry !== None => entry lvl 2
            ...
            # if isDef:
            #     self.entries.get(parentEntry).



if __name__ == '__main__':
    i = index()
    e = Entry('test')
    i.add(e)
    e.addNormalPage(7)
    e.addNormalPage(5)
    e.addPageDef(1)
    e.addPageDef(2)
    e2 = Entry("test22")
    e2.addPageDef(3)
    e2.addPageDef(5)
    e2.addNormalPage(8)
    i.addSubEntry('test' , 'test22') # OR  e.addSubEntry(e2)
    e3 = Entry("osef")

    i.add(e3)
    print(i)