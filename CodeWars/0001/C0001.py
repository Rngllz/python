'''def scramble(s1, s2):
    copia = ''
    for c in s1:
        if c in s2:
            if c in copia:
                if copia.count(c) < s2.count(c) :
                    copia += c
            else:
                copia += c
                
    if len(copia) == len(s2):
        return True
    else:
        return False'''

def scramble(s1, s2):
    lista = list()
    for l in s2:
        lista.append(l)

    n = 0
    for c in s1:
        print(lista)
        if c in lista:
            n += 1
            for i in range(0,int(lista.count(c))):
                lista.remove(c)
            
    print(n)
    print(len(s2))
    if n >= len(s2):
        return True
    else:
        return False
print()
#               r  odlw    world
print(scramble('rkqodlw', 'world') )
print(scramble('cedewaraaossoqqyt', 'codewars'))
print(scramble('katas', 'steak'))
#print(scramble('dvyqyxzfhqpoqu','pvqyqx'))

print()