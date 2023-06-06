def disemvowel(string_):
    
    minus = 'aeiou'
    
    vowels = minus + minus.upper()
    
    noVowels = ''
    
    for s in string_:
        
        if s not in vowels:
            
            noVowels += s
    
    return noVowels