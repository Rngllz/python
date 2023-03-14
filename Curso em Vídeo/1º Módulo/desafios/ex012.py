prec = float(input('Preço do produto: '))
desc = int(input('Desconto a ser dado: '))
print('O valor do produto com {}% de desconto é {:.2f}'.format(desc, prec - ((prec*desc)/100)))