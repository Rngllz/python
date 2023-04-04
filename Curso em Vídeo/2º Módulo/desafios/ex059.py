num1 = 0
num2 = 0
menu = 4

while menu != 5:
    if menu == 4:
        print("\033[32m"+"==-=="*5)
        num1 = int(input("\033[mPrimeiro número: \033[32m"))
        num2 = int(input("\033[mSegundo número: \033[32m"))
        print(""+"==-=="*5)

    print('''\n    \033[33m[1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    \033[31m[5] sair\033[m''')

    menu = int(input("\nOpção: \033[32m"))

    if menu == 1:
        print("\033[mO resultado de {} + {} é igual a: {}".format(num1,num2,num1+num2))
    elif menu == 2:
        print("\033[mO resultado de {} x {} é igual a: {}".format(num1,num2,num1*num2))
    elif menu == 3:
        print("\033[mO maior número entre {} e {} é ".format(num1,num2),end='')
        if num1 > num2:
            print(num1)
        elif num2 > num1:
            print(num2)
        else:
            print("nenhum, pois são iguais.")
    elif menu == 4:
        print("\n\033[32mNOVOS VALORES\033[32")
    elif menu == 5:
        print("\033[31mSISTEMA ENCERRADO!!!\033[m")
    else:
        print("OPÇÃO INVÁLIDA")


