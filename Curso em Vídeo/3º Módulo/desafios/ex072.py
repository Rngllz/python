
número = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove,','dez','onze','doze','treze','quartorze','quinze','dezesseis','dezesete','dezoito','dezenove','vinte')

while True:
    val = int(input("\nDigite um valor de 0 a 20: "))
    while val < 0 or val > 20:
        val = int(input("\033[31mO valor deve ser entre 0 e 20: \033[m"))
    print(f'O seu número escolhido foi o {número[val]}')
    r = ' '
    while r not in 'SN':
        r = str(input('\nContinuar [S/N]: ')).strip().upper()[0]
    if r == 'N':
        break
print("\033[31mPROGRAMA ENCERRADO\033[m")