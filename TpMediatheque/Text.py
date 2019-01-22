from TpMediatheque.Imprimable import Imprimable
from TpMediatheque.Document import Document
#
class Text(Imprimable , Document):

    def __init__(self):
        Imprimable.__init__(self)
        Document.__init__(self)
