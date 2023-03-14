largura = float(input('A largura da parede em metros: '))
altura = float(input('A altura da parede em metros: '))
print('A parede possui {:.2f}m².'.format(largura * altura))
print('Será necessário {:.3f}l de tinta.'.format((largura * altura)/2))