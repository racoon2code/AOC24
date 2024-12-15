def ist_sicher(pegel):
    
    differenzen = [pegel[i+1] - pegel[i] for i in range(len(pegel) - 1)]
    
   
    monoton = all(d > 0 for d in differenzen) or all(d < 0 for d in differenzen)
    
   
    differenz_ok = all(1 <= abs(d) <= 3 for d in differenzen)
    
    return monoton and differenz_ok


result = 0
with open("input.txt", "r") as file:
    for line in file:
        
        pegel = list(map(int, line.strip().split()))
       
        if ist_sicher(pegel):
            result += 1
        else: 
            continue
print(result)

