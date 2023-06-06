def multiplication_table(size):
    
    listiña1 = list(range(1, size + 1))
    
    listiña2 = listiña1
    
    listiña3 = []
    
    for i in listiña1:
        
        aux = []
        
        for j in listiña2:
            
            aux.append(i * j)
            
        listiña3.append(aux)
    
    return listiña3