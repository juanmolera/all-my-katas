def sequence_sum(begin_number, end_number, step):
    
    if begin_number > end_number:
        
        return 0
    
    else:
        
        A = list(range(begin_number, end_number+1, step))
        
        B = sum(A)
        
        return B