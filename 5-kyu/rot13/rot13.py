from string import ascii_lowercase, punctuation


def rot13(message):

    dictio_minus = {}
    original = []
    rotated = []

    message13 = ''

    # diccionario letra: índice de la a-z del 0-25
    for a in ascii_lowercase:

        dictio_minus[a] = ascii_lowercase.index(a)

    
    # se traduce el mensaje a índices del diccionario
    for m in message:
        
        # si el char del mensaje es numérico o un espacio o un signo de puntuación se apendea tal cual como str
        if m.isnumeric() or m.isspace() or m in punctuation:

            original.append(m)
        
        # si el char es mayus se apendea su índice + 26
        elif m.isupper():

            original.append(dictio_minus[m.lower()] + 26)    
    
        # si el char es minus se apendea su índice del diccionario
        else:

            original.append(dictio_minus[m])

    
    # se hacen las rotaciones
    for o in original:

        if type(o) == str:

            rotated.append(o)
        
        # si es minus en la mitad inferior del alfabeto 0-12 pasa a la mitad superior + 13
        elif o <= 12:

            rotated.append(o + 13)
        
        # si es minus en la mitad superior del alfabeto 0-12 pasa a la mitad inferior - 13
        elif o >= 13 and o <= 25:

            rotated.append(o - 13)
        
        # si es mayus
        elif o >= 26 and o <= 38:

            rotated.append(o + 13)
        
        # si es mayus
        elif o >= 39 and o <= 51:

            rotated.append(o - 13)
            

    # para cada índice rotado13
    for r in rotated:
    
        # si es str (num, space or punctuation) se une
        if type(r) == str:

            message13 += r

        else:
            
            # para cada key value del dictio
            for key, value in dictio_minus.items():
                
                # si el índice del rotado es r se apende su key (letra del alfabeto), estas son las minus
                if value == r:

                    message13 += key
                
                # igual para mayus
                elif value == (r - 26) and r >= 26:

                    message13 += key.upper()

                else:

                    pass

    return message13
