from cgi import print_directory
from re import A


frase = 'Curso em Vídeo Python      '
print(frase[::2])



print("""asldkasldkasldkaslkdasda
Aasdasldlasdladskas
dasldkaslkdalsdklsdsdla
asdlaskdlaskdlasdlad
asdlasldasldasldasldasld""")

print(frase.count('o'))
print(frase.upper().count('o'))

print(len(frase.strip()))

print(frase.replace('Curso','Aula'))

print('Curso' in frase)

print(frase.split())
dividido = frase.split()
print('---'.join(dividido))