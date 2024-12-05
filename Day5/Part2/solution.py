from collections import defaultdict, deque


result = 0  


with open("input.txt", "r") as file:
    daten = file.read()


regeln_abschnitt, updates_abschnitt = daten.strip().split("\n\n")


regel_liste = []
for regel in regeln_abschnitt.strip().split("\n"):
    x, y = map(int, regel.split('|'))
    regel_liste.append((x, y))


updates = []
for update in updates_abschnitt.strip().split("\n"):
    updates.append(list(map(int, update.split(','))))


def ist_korrekt_geordnet(update, regeln):
    for x, y in regeln:
        if x in update and y in update:
            if update.index(x) > update.index(y):
                return False
    return True


def topologische_sortierung(update, regeln):
    
    graph = defaultdict(list)
    eingangsgrad = defaultdict(int)
    
    
    for x, y in regeln:
        if x in update and y in update:
            graph[x].append(y)
            eingangsgrad[y] += 1
            if x not in eingangsgrad:
                eingangsgrad[x] = 0

    
    queue = deque([knoten for knoten in update if eingangsgrad[knoten] == 0])
    sortierte_liste = []

    while queue:
        knoten = queue.popleft()
        sortierte_liste.append(knoten)
        for nachbar in graph[knoten]:
            eingangsgrad[nachbar] -= 1
            if eingangsgrad[nachbar] == 0:
                queue.append(nachbar)

    return sortierte_liste



for update in updates:
    if not ist_korrekt_geordnet(update, regel_liste):
        
        korrekt_sortiert = topologische_sortierung(update, regel_liste)
        mitte = len(korrekt_sortiert) // 2
        result += korrekt_sortiert[mitte]

 

print(result)




