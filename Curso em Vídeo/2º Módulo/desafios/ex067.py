n = 0
while True:
    n = int(input("\nDigite um número: "))
    print("\n"+"-"*30)
    if n < 0:
        break
    for c in range(1,11,1):
        print(f" {n} x {c} = {n*c}")
    print("-"*30)
print("Sistema encerrado. VOLTE SEMPRE!!!")