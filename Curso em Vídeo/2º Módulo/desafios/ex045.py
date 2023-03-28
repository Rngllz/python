import random 

vencedor = "Você!!"

rb = random.randint(1,3)

print("\n" + "\033[34m-=-\033[m" * 7)
print("1 - \033[31mPedra\033[m")
print("2 - \033[32mPapel\033[m")
print("3 - \033[33mTesoura\033[m")
print("\033[34m-=-\033[m" * 7)

vc = int(input("Sua escolha: "))

if rb == 1 and vc == 3:
    vencedor = "a Máquina!!"
elif rb == 2 and vc == 1:
    vencedor = "a Máquina!!"
elif rb == 3 and vc == 2:
    vencedor = "a Máquina!!"
elif rb == vc:
    vencedor = "ninguém, ouve um empate!!"


print("\nO vencedor é \033[35m{}\033[m".format(vencedor))
