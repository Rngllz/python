
CFD = False

def avalia_idade(idade: int):
    print(' ')

    if(idade <= 0):
        print('Idade inválida')
    else:

        if(idade <= 13):
            print('Você é uma criança')
        elif(idade <= 17):
            print('Você é um adolescente')
        elif(idade <= 60):
            print('Você é um adulto')
        else:
            print('Você é um idoso') 

        if(idade > 0 and idade < 18):
            print('Por conta de sua idade seu acesso é limitado')
        else:
            print('Você é maior de idade, tem acesso mestre')


while CFD is False: 

    NOME = input('Fale seu nome: ')
    COD = int(input('Digite seu Código: '))
    
    if (NOME == 'Luca' and COD == 123):

        print(' ')
        print('Olá Chefe, bem vindo ao sistema')
        avalia_idade(int(input('Sua idade: ')))
        CFD = True

    else:
        print('Acesso negado')