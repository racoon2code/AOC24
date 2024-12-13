result = 0

def string_zu_gitter(zeilen_string):
    return zeilen_string.strip().split('\n')

def berechne_koordinaten(start, richtung, wort):
    x, y = start
    dx, dy = richtung
    koordinaten = []
    for i in range(len(wort)):
        koordinaten.append((x + i * dx, y + i * dy))
    return koordinaten

def ist_gueltig(koordinaten, zeilen, spalten):
    for x, y in koordinaten:
        if not (0 <= x < zeilen and 0 <= y < spalten):
            return False
    return True

def lese_zeichen_aus_gitter(gitter, koordinaten):
    return [gitter[x][y] for x, y in koordinaten]


with open("input.txt", "r") as file:
    gitter = string_zu_gitter(file.read())

zeilen = len(gitter)
spalten = len(gitter[0])
richtungen = [
    (0, 1),   # Horizontal nach rechts
    (0, -1),  # Horizontal nach links
    (1, 0),   # Vertikal nach unten
    (-1, 0),  # Vertikal nach oben
    (1, 1),   # Diagonal unten rechts
    (1, -1),  # Diagonal unten links
    (-1, 1),  # Diagonal oben rechts
    (-1, -1)  # Diagonal oben links
]

for zcount, z  in enumerate(gitter):
    
    for scount, s in enumerate(gitter[0]):
        start = (zcount, scount)
        
        for r in richtungen:
            
            koordinaten = berechne_koordinaten(start, r, "XMAS")
            

            if ist_gueltig(koordinaten, zeilen, spalten):
                zeichen = lese_zeichen_aus_gitter(gitter, koordinaten)
                wort = ''.join(zeichen)
                if wort == "XMAS":
                    result += 1
                else: 
                    continue

            else:
                continue


print(result)
