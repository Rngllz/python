alunos = {'Pedro': 8.0, 'Maria': 10.0, 'Amilton': 7.5}


with open('exercícios/txt/ex15.txt','w') as txt:
    for k,v in alunos.items():
        txt.write(f'Aluno: {k} \t|  Nota: {v}\n')


with open('exercícios/txt/ex15.txt', 'r') as txt:
    for linhas in txt:
        print(linhas,end='')