

class Estudante:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
        self.notas = []
    
    def obterMedia(self):
        MEDIA = sum(self.notas) / len(self.notas)
        return MEDIA

est1 = Estudante('Luca',17)
est1.notas = [9,2,7]

print('')
print('Nome do estudante:',est1.nome)
print('Idade do estudante:',est1.idade)
print('Notas do estudante:',est1.notas)
print('Média do estudantte:',est1.obterMedia())
print('')

class Computador:
    def __init__(self,marca,memoria_ram,placa_de_video):
        self.marca = marca
        self.memoria_ram = memoria_ram
        self.placa_de_video = placa_de_video

    def Ligar(self):
        print('estou ligando')

    def Desligar(self):
        print('Estou desligando')

    def ExibirInfo(self):
        print(self.marca,self.memoria_ram,self.placa_de_video)

computador1 = Computador('Asus','16gb','Nvidia')
computador1.Ligar()
computador1.Desligar()
computador1.ExibirInfo()