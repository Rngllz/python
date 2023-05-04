from ex111_.utilidadesCev.dado import dado 
from ex111_.utilidadesCev.moeda import moeda

p = dado.leiaDinheiro('Digite o preço: R$')
moeda.resumo(p, 80, 35)