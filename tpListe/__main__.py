from tpListe.ListePriorite import ListePriorite
import copy

print('starting')
list = ListePriorite()
list.add(2,"hello")
list.add(1,"bonjour")
list.add(3,"bye")
list.add(0,"bye")
print(list.prio_max)
print(list.prio_min)
print(list.contains("bye"))
print(list.contains("by"))
print(list.priorities_of('bye'))
#fonctionne aussi :print("bye" in list)
print(list)
print(list.empty)
print(list.pop())
print(list)
print(list.length)
list2 = copy.deepcopy(list)
list2.add(9,'test')
print (list)
print (list2)
