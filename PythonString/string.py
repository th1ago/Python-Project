url = "bytebank.com/cambio?moedaDestino=dolar&moedaOrigem=real"

# Sanitizacao da URL
url = url.strip()

# Validacao da URL
if url == "":
    raise ValueError("A URL esta vazia")

# separa base e param
indice_interrogacao = url.find('?')
url_base = url[:indice_interrogacao]
# como e inclusivo devo colocar o +1
url_parametros = url[indice_interrogacao+1:] # moedaOrigem=real
print(url_parametros)

parametro_busca = "moedaDestino"
indice_parametro = url_parametros.find(parametro_busca) # moedaDestino=dolar&moedaOrigem=real = 18
indice_valor = indice_parametro + len(parametro_busca) + 1 # moedaOrigem=real = 12
indice_e_comercial = url_parametros.find("&", indice_valor)
if indice_e_comercial == -1: # verifica se possui & depois ou nao
    valor = url_parametros[indice_valor:]
else:
    valor = url_parametros[indice_valor:indice_e_comercial]
print(valor)