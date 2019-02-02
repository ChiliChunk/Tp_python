class Entry:
    def __init__(self ,title):
        self.title = title
        self.defPage = set()
        self.normalPage = set()
        self.subEntry = set()

    def addPageDef(self,number):
        self.defPage.add(number)

    def addNormalPage(self,number):
        self.normalPage.add(number)

    def addSubEntry(self,entry):
        self.subEntry.add(entry)


    def __str__(self):
        result = ""+self.title+" : "
        for page in sorted(list(self.defPage)):
            result += "*"+str(page)+"* "

        for page in sorted(list(self.normalPage)):
            result += str(page) +' '

        for entry in self.subEntry:
            result += "\n   "+entry.__str__()
        result += "\n"
        return result