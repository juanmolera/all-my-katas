import re

def to_cents(amount):
    
    if bool(re.fullmatch('\$\d+\.\d{2}', amount)):
        
        x = amount.replace("$", "").replace(".", "")
        
        return int(x)