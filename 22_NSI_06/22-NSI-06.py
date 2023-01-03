# ex 1
def maxi(tab):
    resultat = (tab[0], 0)
    for i in range(len(tab)):
        if tab[i] > resultat[0]:
            resultat = (tab[i], i)
    return resultat

#print(maxi([1,5,6,9,1,2,3,7,9,8]))

def recherche(gene, seq_adn):
    n = len(seq_adn)
    g = len(gene)
    i = 0
    trouve = False
    while i < n and trouve == False :
        j = 0
        while j < g and gene[j] == seq_adn[i+j]:
            j += 1
        if j == g:
            trouve = True
        i += 1
    return trouve

print(recherche("voice", "Over the carnage rose a voice prophetic"))
