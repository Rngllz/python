caracteres = []

expressao = str(input('\nDigite uma expressão com parênteses: '))
for c in expressao:
    caracteres.append(c)

if caracteres.count('(') == caracteres.count(')'):
    print('Esta expressão é válida\n')
else:
    print('Esta expressão é inválida\n')


# Código do professor 

expr = str(input('Digite a expressão: '))
pilha = []
for símb in expr:   # Lógicas diferentes, porém não ouve diferança nos resultados
    if símb == '(':
        pilha.append('(')
    elif símb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')

