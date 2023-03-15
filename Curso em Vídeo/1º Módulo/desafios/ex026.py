frase = str(input('Digite uma frase: ')).strip().lower()

print('A letra "a" aparece {} vezes na frase.\nA primeira aparição é na posição: {}.\nSua última é na posição: {}.'.format(frase.count('a'), frase.find('a')+1, frase.rfind('a')+1))