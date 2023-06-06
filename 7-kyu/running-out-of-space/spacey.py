def spacey(array):
    
    res = []
    
    last = ''
    
    for i in array:
        
        res.append(last + i)
        
        last += i
    
    return res