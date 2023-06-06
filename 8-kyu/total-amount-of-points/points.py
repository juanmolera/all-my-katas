def points(games):
    
    points = 0
    
    # i = x:y
    for i in games:
        
        # si gana x, nuestro equipo suma 3 puntos:
        if i[0] > i[2]:
            
            points += 3
        
        # si empata x, nuestro equipo suma 1 punto:
        elif i[0] == i[2]:
            
            points += 1
        
        # si pierde x, pues na
        else:
            
            pass
        
    return points