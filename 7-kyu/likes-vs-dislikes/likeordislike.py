def like_or_dislike(lst):

    # si no se ha pulsado ningún botón, se devuelve nada
    if len(lst) == 0:
        
        return Nothing
    
    # si se ha pulsado solo 1 vez, se devuelve el último
    elif len(lst) == 1:
        
        return lst[-1]
    
    # si se ha pulsado más de 1 vez:
    else:
        
        last = None
        
        for i in lst:
            
            # si el siguiente es igual al anterior, devuelve nada
            if i == last:
                
                last = 'Nothing'
            
            # si el siguiente es diferente, se cambia
            else:
                
                last = i
        
        return last