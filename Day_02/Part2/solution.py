def ist_sicher(pegel):
    differenzen = [pegel[i+1] - pegel[i] for i in range(len(pegel) - 1)]
    
    
    monoton = all(d > 0 for d in differenzen) or all(d < 0 for d in differenzen)
    
   
    differenz_ok = all(1 <= abs(d) <= 3 for d in differenzen)
    
    return monoton and differenz_ok

def ist_sicher_mit_dämpfer(pegel):
    
    if ist_sicher(pegel):
        return True
    
    
    for i in range(len(pegel)):
        modifiziert = pegel[:i] + pegel[i+1:]  
        if ist_sicher(modifiziert):
            return True
    
    return False

result = 0

with open("input.txt", "r") as file:
    for line in file:
        
        pegel = list(map(int, line.strip().split()))
       
        if ist_sicher_mit_dämpfer(pegel):
            result += 1
        else: 
            continue
print(result)