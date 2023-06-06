from string import ascii_lowercase, punctuation

# 0-12, 13-25, 26-38, 39-51

def rot13(message):
    pass

dictio_minus = {}
original = []
rotated = []

message = 'EBG13 rknzcyr.'
#message = 'Guvf vf npghnyyl gur svefg xngn V rire znqr. Gunaxf sbe svavfuvat vg! :)'

message13 = ''

for a in ascii_lowercase:
        
    dictio_minus[a] = ascii_lowercase.index(a)


for m in message:

    if m.isnumeric() or m.isspace() or m in punctuation:

        original.append(m)

    elif m.isupper():
        
        original.append(dictio_minus[m.lower()] + 26)    

    else:

        original.append(dictio_minus[m])


print(original)


for o in original:

    if type(o) == str:

        rotated.append(o)

    elif o <= 12:

        rotated.append(o + 13)

    elif o >= 13 and o <= 25:

        rotated.append(o - 13)

    elif o >= 26 and o <= 38:

        rotated.append(o + 26)

    elif o >= 39 and o <= 51:

        rotated.append(o - 26)


print(rotated)


for r in rotated:

    if type(r) == str:

        message13 += r

    else:

        for key, value in dictio_minus.items():

            if r == value and r <= 25:
                
                message13 += key
            
            elif r == (value - 26) and  r >= 26:

                message13 += key.upper()

            else:

                pass


print(message13)