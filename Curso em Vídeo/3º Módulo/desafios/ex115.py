from ex115_.telas import telas 
from time import sleep

while True:
    sleep(2)
    for i in range (21):
        print()
    opc = telas.menu_principal()
    if opc == 1:
        telas.pessoas_cadastradas()
    elif opc == 2:
        telas.novo_cadastro()
    elif opc == 3:
        print('     \033[31mX Encerrando o sistema... X\033[m')
        break
