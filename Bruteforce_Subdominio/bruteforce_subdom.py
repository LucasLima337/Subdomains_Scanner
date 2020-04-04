import sys
import dns.resolver

try:
    dominio = sys.argv[1]
    wordlist = sys.argv[2]
except:
    print('Faltam Argumentos!')
    sys.exit()

try:
    lista = open(wordlist).read()
    lista = lista.splitlines()
except:
    print('Wordlist não encontrada!')
    sys.exit()

for linha in lista:
    sub = f'{linha}.{dominio}'
    try:
        ip = dns.resolver.query(sub, 'a')
        for site in ip:
            print(f'{sub} {site}')
    except:
        pass
