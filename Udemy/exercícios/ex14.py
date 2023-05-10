nums = list()

while True:
    try:
        nums.clear()
        nums.append(float(input('1º Número: ')))
        nums.append(float(input('2º Número: ')))
        print(nums)
        r = nums[1] / nums[0]
    except ValueError:
        print('ERRO! Caracter inválido!')
    except ZeroDivisionError:
        print('ERRO! Divisão por zero é inválida!')
    except IndexError:
        print('ERRO! Posições inválidas!')
    except KeyboardInterrupt:
        print('O sistema foi interrompido!')
    else:
        print(f'O resultado é {r}')