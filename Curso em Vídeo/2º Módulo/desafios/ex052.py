from time import sleep

n = int(input("Número: "))

tf = True

for c in range(1,n+1,1):
        
    if n%c == 0:    
        if c != 1 and c != n:
            tf = False
        print("\033[32m{}".format(c),end=' ')
    else:
        print("\033[31m{}".format(c),end=' ')
    
print("\033[m- É um Número primo" if tf else "\033[m- Não é um Número primo")
sleep(10)