from bytebank import Funcionario

class TestCalss:
    """criando class de teste"""
    def test_quando_idade_recebe_01_01_2000_retorna_23(self):
        """teste quando idade for igual a 23"""
        entrada = "01/01/2000"
        esperado = 23

        funcionario_teste = Funcionario("Thiago", entrada, 1000)
        resultado = funcionario_teste.idade()
        # verifica se o que estou passando 'e verdade ou nao
        assert resultado == esperado

    def test_separando_nome_do_sobrenome(self):
        """teste quando idade for igual a 23"""
        entrada = "Thiago Silva"
        esperado = "Silva"

        funcionario_teste = Funcionario(entrada, "01/01/2000", 1000)
        resultado = funcionario_teste.sobrenome()
        # verifica se o que estou passando 'e verdade ou nao
        assert resultado == esperado
