class Entry:
    def __init__(self ,title):
        self.title = title
        self.defPage = []
        self.normalPage = []
        self.subEntry = []

    def addPageDef(self,number):
        if number not in self.defPage:
            self.defPage.append(number)
            self.defPage.sort()
    
    def addNormalPage(self,number):
        if number not in self.normalPage:
            self.normalPage.append(number)
            self.normalPage.sort()

    def addSubEntry(self,entry):
        self.subEntry.append(entry)


    def __str__(self):
        result = ""+self.title+" : "
        for page in self.defPage:
            result += "*"+str(page)+"* "

        for page in self.normalPage:
            result += str(page) +' '

        for entry in self.subEntry:
            result += "\n   "+entry.__str__()
        result += "\n"
        return result