idades = [21, 22, 23]
idades.extends([27, 19])
#idades.remove(15) Error


for idade in idades:
    print(idade)

# SOMAR + 1
idades_ano_que_vem = []
for idade in idades:
    idades_ano_que_vem.append(idade + 1)
idades_ano_que_vem

# outra forma de faver - SOMAR + 1
idades_ano_que_vem = [(idade + 1) for idade in idades]

# Procurar numeros maior que 21
def proximo_ano(idade):
    return idade + 1
[proximo_ano(idade) for idade in idades if idade > 21]

# DESSA MANEIRA, COM ESSES COLCHETES E CRIADO UMA NOVA LISTA
# 'E CHAMADA DE LIST COMPREHESION, INTERANDO POR DIVERSOS ELEMENTOS