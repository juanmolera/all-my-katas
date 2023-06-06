from string import ascii_lowercase

def is_pangram(s):
    
    return all([char in s.lower() for char in ascii_lowercase])