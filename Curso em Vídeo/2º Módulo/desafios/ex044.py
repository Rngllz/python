preco = float(input("\nPreço do produto: \033[4;32m"))

print("\033[m\n" + "\033[2;32m+=\033[m" * 11)
print("1 - Á vista (dinheiro)")
print("2 - Á vista (cartão)")
print("3 - Parcelado")
print("\033[2;32m+=\033[m" * 11)

forma = int(input("\nForma de pagamento: "))

if forma == 1:
    valor = preco - (preco * 10 / 100) 
    print("\nO valor a ser pago é: \033[2;32m{:.2f} R$\033[m.\n".format(valor))
elif forma == 2:
    valor = preco - (preco * 5 / 100)
    print("\nO valor a ser pago é: \033[2;32m{:.2f} R$\033[m.\n".format(valor))
elif forma == 3:
    parcela = int(input("Quantidade de parcelas:"))
    if parcela <= 2:
        valor = preco
    else:
        valor = (preco * 20 / 100) + preco
    print("\nO valor por parcela ({}) é: \033[2;32m{:.2f} R$\033[m.".format(parcela, valor / parcela),end='')
    print("\nO valor a ser pago é: \033[2;32m{:.2f} R$\033[m.\n".format(valor))
else:
    print("\n" + "\033[31m#"*30)
    print(("{:=^30}").format(" OPÇÃO INVÁLIDA "))
    print("#"*30+"\033[m")
    