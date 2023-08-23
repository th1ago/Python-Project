conta_thiago = (100, 1)


def deposita(conta): # varicao funcional(separando o comportamento dos dados)
    nova_conta = conta[1] + 100
    codigo = conta[1]
    return(nova_conta, codigo)

teste = deposita(conta_thiago)
print(teste)
