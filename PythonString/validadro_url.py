import re

url = 'https://www.bytebank.com.br/cambio'
# Utilizando parênteses, estou falando que aquele conjunto tem que ser exatamente aqueles caracteres
padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio') 
match = padrao_url.match(url)

if not match:
    raise ValueError("A URL nao e valida")