result = 0

with open("input.txt", "r") as file:
    daten = file.read()


regeln_abschnitt, updates_abschnitt = daten.strip().split("\n\n")


regel_liste = []
for regel in regeln_abschnitt.strip().split("\n"):
    x, y = map(int, regel.split('|'))
    regel_liste.append((x, y))


def ist_korrekt_geordnet(update, regeln):
    for x, y in regeln:
        if x in update and y in update:
            if update.index(x) > update.index(y):
                return False
    return True

updates = []
for update in updates_abschnitt.strip().split("\n"):
    updates.append(list(map(int, update.split(','))))

for update in updates:
    if ist_korrekt_geordnet(update, regel_liste):
        mitte = len(update) // 2
        result += update[mitte]

print(result)
