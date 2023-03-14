metro = float(input('Digite um valor em metros: '))
print('A medida de {}m corresponde a'.format(metro))
print('{}km\n{}hm\n{}dam\n{}dm\n{}cm\n{}mm'.format((metro/1000), (metro/100), (metro/10), (metro*10), (metro*100), (metro*1000)))