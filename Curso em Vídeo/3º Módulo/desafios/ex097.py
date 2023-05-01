
def escreva(txt):
    tamanho = len((txt).strip())
    print()
    print('~'*(tamanho+10))
    print(f'{(txt).strip():^{tamanho+10}}')
    print('~'*(tamanho+10))

escreva('Luca Mateo Rangel')
escreva('Luca      ')
escreva('ALasdlkalsdalskdlaksdlaklslsldlassl')