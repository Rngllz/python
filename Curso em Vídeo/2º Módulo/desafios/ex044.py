preco = float(input("\nPreço do produto: "))

print("\n" + "\033[2;32m+=\033[m" * 11)
print("1 - Á vista (dinheiro)")
print("2 - Á vista (cartão)")
print("3 - Parcelado (2x)")
print("4 - Parcelado (3x +)")
print("\033[2;32m+=\033[m" * 11)

forma = int(input("\nForma de pagamento: "))

if forma == 1:
    valor = preco - (preco * 10 / 100) 
elif forma == 2:
    valor = preco - (preco * 5 / 100)
elif forma == 3:
    valor = preco
else:
    valor = (preco * 20 / 100) + preco


print("\nO valor a ser pago é: \033[2;32m{:.2f} R$\033[m.".format(valor))