nota1 = float(input("Primeira nota: "))
nota2 = float(input("Segunda nota: "))

if (nota1 + nota2)/2 < 5:
    print("\033[1;31mREPROVADO\033[m")
elif (nota1 + nota2)/2 <= 6.9:
    print("\033[1;33mRECUPERAÇÃO\033[m")
else:
    print("\033[1;32mAPROVADO\033[m")