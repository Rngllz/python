'''teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(teste)
print(galera)'''


'''galera = [['João',19],['Ana',33],['Joaquim',13],['Maria',45]]
print(galera[0])
print(galera[0][0])
print(galera[3][0])

for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade')'''


galera = list()
dado = list()
totmai = totmen = 0
for c in range(0,3):
    dado.append(str(input('Nome: ')))
    dado.append(str(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()

for p in galera:
    if int(p[1]) >= 21:
        print(f'{p[0]} é maior de idade.')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmen += 1
print(galera)
print(f'Temos {totmai} maiores de idade e {totmen} menores.')