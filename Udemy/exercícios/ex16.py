import re

frase = 'Minha casa fica na rua Carneiro, 78. O CEP é 88388-000 e meu site é https://www.iaexpert.academy'

print(re.search('\d{2}',frase))
print(re.search('\d{5}-\d{3}',frase))
print(re.search('https?://[A-Za-z0-9\.]+',frase))