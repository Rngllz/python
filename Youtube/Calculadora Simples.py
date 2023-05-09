NUMERO1 = 0
NUMERO2 = 0
OPERACAO = ''
RESULTADO = 0.0

NUMERO1 = int(input('Digite o primeiro número: '))

while OPERACAO != '+' and OPERACAO != '-' and OPERACAO != '/' and OPERACAO != '*':

    print('')
    print('     + Adição')
    print('     - Subtração')
    print('     / Divisão')
    print('     * Multiplicação')
    print('')
    OPERACAO = str(input('Digite a operação a ser feita: '))
    print('')

NUMERO2 = int(input('Digite o segundo número: '))
print('')

if(OPERACAO == '+'):
    RESULTADO = NUMERO1 + NUMERO2
elif(OPERACAO == '-'):
    RESULTADO = NUMERO1 - NUMERO2
elif(OPERACAO == '/'):
    RESULTADO = NUMERO1 / NUMERO2
elif(OPERACAO == '*'):
    RESULTADO = NUMERO1 * NUMERO2  



print('O resultado de '+str(NUMERO1)+' '+str(OPERACAO)+' '+str(NUMERO2)+' é: '+str(RESULTADO))
print('')