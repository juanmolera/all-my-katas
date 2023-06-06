def expanded_form(num):
    
    res = ''
    
    count = 1
    
    string = str(num)[::-1]
    
        
    for s in string:
        
        n = int(s)
        
        if n == 0:
            pass
        
        else:
            res = str(n*count) + ' + ' + res
        
        count *= 10
    
    res = res.rstrip(' + ')
    
    return res