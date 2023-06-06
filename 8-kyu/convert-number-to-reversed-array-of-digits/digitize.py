def digitize(n):

    lista=[]
    
    for i in str(n):

        lista.append(int(i))
        
    return lista[::-1]