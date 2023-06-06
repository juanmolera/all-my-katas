from string import ascii_lowercase, punctuation

# 0-12, 13-26, 27-39, 40-53

def rot13(message):
    pass

dictio_minus = {}

original = []
rotated = []

#message = 'EBG13 rknzcyr.'
message = 'Guvf vf npghnyyl gur svefg xngn V rire znqr. Gunaxf sbe svavfuvat vg! :)'

message13 = ''

for a in ascii_lowercase:
        
    dictio_minus[a] = ascii_lowercase.index(a)


for m in message:

    if m.isnumeric() or m.isspace():

        original.append(m)

    elif m in punctuation:

        original.append(m)

    elif m.isupper():
        
        original.append(dictio_minus[m.lower()] + 26)    

    else:

        original.append(dictio_minus[m])


for o in original:

    if type(o) == str:

        rotated.append(o)

    elif o < 13:

        rotated.append(o + 13)

    elif o >= 13 and o < 26:

        rotated.append(o - 13)

    elif o >= 26 and o < 40:

        rotated.append(o + 26)

    elif o >= 40 and o < 52:

        rotated.append(o - 26)

print(original)

print(rotated)


for r in rotated:

    if type(r) == str:

        message13 += r

    else:

        for key, value in dictio_minus.items():
            
            if r == value and r < 26:
                
                message13 += key
            
            else:

                 message13 += key.upper()


print(message13)
