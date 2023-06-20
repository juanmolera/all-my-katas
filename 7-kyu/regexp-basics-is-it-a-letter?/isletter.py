import re

def is_letter(s):
    
    return bool(re.fullmatch('[a-z]{1}|[A-Z]{1}', s))