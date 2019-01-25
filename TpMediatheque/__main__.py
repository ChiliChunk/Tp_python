from TpMediatheque.Mediatheque import Mediatheque
from TpMediatheque.Livre import Livre

mediat = Mediatheque()
mediat.listDocument = Mediatheque.restore('mediatheque.dat')
...
...
if mediat.listDocument != Mediatheque.restore('mediateque.dat'):
    mediat.sauve('mediatheque.dat')

