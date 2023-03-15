from math import sin, cos, tan, radians

ang = float(input('Digite um ângulo qualquer: '))
print('Seu seno é {:.2f}\nSeu consseno é {:.2f}\nSua tangente é {:.2f}'.format(sin(radians(ang)), cos(radians(ang)), tan(radians(ang))))