saludos = ['hello', 'ciao', 'salut', 'hallo', 'hola', 'ahoj', 'czesc']

def validate_hello(greetings):

    res = False
    
    for i in saludos:

        if i in greetings.lower():

            res = True
            
    return res