def duplicates(arr):
    
    no_duplicados = []
    duplicados = []
    
    for a in arr:
        if a not in no_duplicados:
            no_duplicados.append(a)
            
        else:
            if a not in duplicados:
                duplicados.append(a)
            
    return duplicados