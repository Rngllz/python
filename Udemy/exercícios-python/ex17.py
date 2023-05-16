class Aluno:
    def __init__(self,nome,nota1,nota2):
        self.nome = nome
        self.nota_1 = nota1
        self.nota_2 = nota2
        self.media = 0.0


    def faz_media(self):
        self.media = (self.nota_1 + self.nota_2) / 2
        return self.media
    

    def mostra(self):
        print(f'Nome: {self.nome}\n1ª nota: {self.nota_1}\n2ª nota: {self.nota_2}\nMédia: {self.media}')

    
    def veri_media(self):
        return 'Aprovado' if self.media >= 6 else 'Reprovado'



aluno1 = Aluno('Luca',4,7)
aluno1.faz_media()
aluno1.mostra()
print(aluno1.veri_media())

aluno2 = Aluno('Pedro',10,8)
aluno2.faz_media()
aluno2.mostra()
print(aluno2.veri_media())