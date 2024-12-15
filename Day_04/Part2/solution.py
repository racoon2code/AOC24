def string_zu_gitter(zeilen_string):
    return zeilen_string.strip().split('\n')

def finde_x_mas(gitter):
    
    zeilen = len(gitter)
    spalten = len(gitter[0]) if zeilen > 0 else 0
    
    
    oben_links_unten_rechts = [(-1, -1), (1, 1)]
    unten_links_oben_rechts = [(1, -1), (-1, 1)]
    
    result = 0  
    
    
    for x in range(1, zeilen - 1):
        for y in range(1, spalten - 1):
            
            if (
                pruefe_diagonale(gitter, x, y, oben_links_unten_rechts, "MAS") or
                pruefe_diagonale(gitter, x, y, oben_links_unten_rechts, "SAM")
            ) and (
                pruefe_diagonale(gitter, x, y, unten_links_oben_rechts, "MAS") or
                pruefe_diagonale(gitter, x, y, unten_links_oben_rechts, "SAM")
            ):
                result += 1  
    
    return result


def pruefe_diagonale(gitter, x, y, bewegung, wort):
    
    (dx1, dy1), (dx2, dy2) = bewegung
    
    
    try:
        return (gitter[x + dx1][y + dy1] == wort[0] and
                gitter[x][y] == wort[1] and
                gitter[x + dx2][y + dy2] == wort[2])
    except IndexError:
        return False  

with open("input.txt", "r") as file:
    gitter = string_zu_gitter(file.read())

print(finde_x_mas(gitter))




