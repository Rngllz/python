
try: # Tenta fazer rodar o código
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b

except (ValueError, TypeError): # Caso de algum erro
    print(f'Os dados informados são inválidos.')

except ZeroDivisionError: # Caso de algum erro
    print(f'Não é possível dividir por zero.')

except Exception as erro:
    print(f'Ocorreu um erro genérico: {erro.__class__}')

else: # Caso não de nenhum erro
    print(f'O resultado é {r}') 
    
finally: # Não importa o que aconteça, ele entra aqui
    print('Volte sempre! Muito obrigado!')


