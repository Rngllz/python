num = [2,5,9,1]
num[0] = 100
num.pop()
num.append(7)
num.sort()
num.insert(0,5)
num.remove(5)
if 120 in num:
    num.remove(120)
print(num) 

print('\n\n\n')

#valores = []
#valores.append(5)
#valores.append(9)
#valores.append(4)
#for c in range(1,6):
#    valores.append(int(input("Digite um número: ")))

#or n,c in enumerate(valores):
#    print(f'{n+1}-{c}...',end='')


a = [2,3,4,5]
b = a[:]
b[0] = 100
print(a)
print(b)