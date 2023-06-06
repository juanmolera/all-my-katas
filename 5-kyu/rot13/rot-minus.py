from string import ascii_lowercase, ascii_uppercase, punctuation

def rot13(message):
    pass

dictio_minus = {}
dictio_mayus = {}

original = []
rotated = []

#message = 'EBG13 rknzcyr.'
message = 'Guvf vf npghnyyl gur svefg xngn V rire znqr. Gunaxf sbe svavfuvat vg! :)'

message13 = ''

for a in ascii_lowercase:
        
    dictio_minus[a] = ascii_lowercase.index(a)

for b in ascii_uppercase:
        
    dictio_mayus[b] = ascii_uppercase.index(b)
    
for m in message:

    if m.isnumeric() or m.isspace():

        original.append(m)

    elif m in punctuation:

        original.append(m)

    elif m.isupper():
        
        original.append(dictio_mayus[m])    

    else:

        original.append(dictio_minus[m])


for o in original:

    if type(o) == str:

        rotated.append(o)

    elif o < 13:

        rotated.append(o + 13)

    else:

        rotated.append(o - 13)

print(original)

print(rotated)


for r in rotated:

    if type(r) == str:

        message13 += r

    else:

        for key, value in dictio_minus.items():

            if r == value:
            
                message13 += key


print(message13)
