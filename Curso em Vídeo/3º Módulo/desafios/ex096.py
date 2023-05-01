

def área(a,b):
    c = a * b
    print('    '+'-'*50)
    print(f'    A área do terreno {a:.1f}m x {b:.1f}m é igual a {c:.1f}m²')
    print('    '+'-'*50)


largura = comprimento = 0

print()
largura = float(input('    Largura (m): '))
comprimento = float(input('    Comprimento (m): '))
área(largura,comprimento)
print()