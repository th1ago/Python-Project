from bytebank import Funcionario

def teste_idade():
    """automatizacao"""
    thiago = Funcionario("Thiago", '01/01/2000', 1000)
    print(f'teste = {thiago.idade()}')

teste_idade()