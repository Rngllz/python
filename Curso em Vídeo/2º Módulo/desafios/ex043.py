peso = float(input("\nSeu peso: "))
altura = float(input("Sua altura: "))

imc = peso / (altura ** 2)

print("\nVocê possui o \033[2;31mIMC\033[m {:.2f}, você tem: ".format(imc),end='')

if imc <= 18.5:
    print("\033[3;32mPeso abaixo do normal.\033[m\n")
elif imc <= 25:
    print("\033[3;33mPeso Ideal.\033[m\n")
elif imc <= 30:
    print("\033[3;34mSobrepeso.\033[m\n")
elif imc <= 40:
    print("\033[3;35mObesidade.\033[m\n")
else:
    print("\033[3;36mObesidade Mórbida.\033[m\n")