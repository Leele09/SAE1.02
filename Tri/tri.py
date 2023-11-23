# Module contenant un ensemble de tri

# Tri_gnome
def tri_gnome(d):
    i,j = 1,2
    while i < len(d):
        if d[i-1] <= d[i]:
            i = j
            j = j+1
        else:
            d[i-1],d[i] = d[i],d[i-1]
            i -= 1
            if i == 0:
                i,j = j,j+1
    return d

# Tri shaker
def tri_shaker(tab):
    trie = True
    debut , fin = 0 , len(tab)-1

    # Tant que la liste n'est pas triée
    while trie == True:
        trie = False
        # On trie de l'extrémité gauche à droite (tri bulle croissant)
        for i in range(debut, fin):
            if tab[i] > tab[i+1]: # On échange si la valeur antécédente est supérieur à celle d'après
                tab[i], tab[i+1]= tab[i+1], tab[i]
                trie = True
        fin -= 1 # On décrémente de 1 la borne de fin

        # On trie dans l'ordre inverse (tri bulle décroissant)
        for u in range(fin, debut,-1): # On échange si la valeur d'après est inférieur à celle d'avant
            if tab[u] < tab[u-1]:
                tab[u] , tab[u-1] = tab[u-1], tab[u]
                trie = True
        debut += 1 # On incrémente de 1 la borne de debut

    return tab

# Tri rapide
def tri_rapide(L):
    if len(L)==1 or len(L)==0:
        return L
    pivot=L[len(L)//2]
    L_inf=[x for x in L if x < pivot]
    L_sup=[x for x in L if x > pivot]
    return tri_rapide(L_inf)+[pivot]+tri_rapide(L_sup)

# Tri selection
def tri_selection(nums):
    for i in range(len(nums)):
        min_idx = i
        for j in range(i+1, len(nums)):
            if nums[min_idx] > nums[j]:
                min_idx = j
        nums[i], nums[min_idx] = nums[min_idx], nums[i]
    return nums

# Tri fusion
def tri_fusion(l):
    if len(l) > 1:
        m = len(l) // 2
        g = l[:m]
        d = l[m:]

        tri_fusion(g)
        tri_fusion(d)

        i, j, k = 0, 0, 0
        while i < len(g) and j < len(d):
            if g[i] < d[j]:
                l[k] = g[i]
                i = i + 1

            else:
                l[k] = d[j]
                j = j + 1
            k = k + 1
        while i < len(g):
            l[k] = g[i]
            i = i + 1
            k = k + 1
        while j < len(d):
            l[k] = d[j]
            j = j + 1
            k = k + 1
        return l

# Tri insertion
def tri_insertion(L):
    for i in range(1,len(L)):
        while L[i-1] > L[i] and i > 0:
            L[i-1] , L[i] = L[i] , L[i-1]
            i = i - 1
    return L

# Tri bulle
def tri_bulle(b):
    permute = True
    entree = 0
    while permute == True:
        permute = False
        entree = entree + 1
        for i in range(0, len(b) - entree):
            if b[i] > b[i + 1]:
                permute = True
                b[i], b[i + 1] = b[i + 1],b[i]
    return b
