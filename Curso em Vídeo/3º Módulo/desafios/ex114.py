import urllib
import urllib.request

try: 
    site = urllib.request.urlopen('http://www.pudim.com.br/')
except:
    print('\033[31mO site não está acessível no momento\033[m')
else:
    print('\033[32mO site está acessível no momento\033[m')