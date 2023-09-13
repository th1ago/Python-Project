'''teste bytebank'''
import pytest
from pytest import mark
from codigo.bytebank import Funcionario

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

    def test_decrescimo_salario_quando_receber_10000_retorna_9000(self):
        """verifica se eh socio e realiza o decrescimo"""
        entrada_salario = 10000 #given
        entrada_nome = "Paulo Silveira"
        esperado = 9000

        funcionario_teste = Funcionario(entrada_nome, "01/01/2000", entrada_salario)
        # Atribuindo resultado de uma chamada de função, onde a função não tem retorno
        funcionario_teste.decrescimo_salario() #when
        resultado = funcionario_teste.salario

        assert resultado == esperado #then

    @mark.calcular_bonus
    def test_salario_for_igual_1000_retorna_100(self):
        """verifica bonus se for ate 1000 e aplica 10%"""
        entrada = 1000 #given
        esperado = 100

        funcionario_teste = Funcionario("Thiago", "01/01/2000", entrada)
        resultado = funcionario_teste.calcular_bonus() #when

        assert resultado == esperado #then

    @mark.calcular_bonus
    def test_salario_for_igual_10000000_retorna_valueerror(self):
        """verifica bonus se for ate 1000 e aplica 10%"""
        with pytest.raises(ValueError):
            entrada = 1000000 #given

            funcionario_teste = Funcionario("Thiago", "01/01/2000", entrada)
            resultado = funcionario_teste.calcular_bonus() #when

            assert resultado#then
