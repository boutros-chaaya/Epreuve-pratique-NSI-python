def recherche(elt, tab):
    index = -1
    for i in range(len(tab)):
        if tab[i] == elt:
          index = 1
    return index

#print(recherche(1, [10, 12, 1, 56]))

def insere(a, tab):
    l = list(tab) #l contient les mêmes éléments que tab
    l.append(a)
    i = len(l) - 1
    while a < l[i] and i >= 0: 
      l[i+1] = l[i] 
      l[i] = a
      i = i - 1
    return l

print(insere(1,[2,3,4]))