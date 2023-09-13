'''criando o bytebank'''
from datetime import date

class Funcionario:
    """declaracao da classe"""
    def __init__(self, nome, data_nascimento, salario):
        self._nome = nome
        self._data_nascimento = data_nascimento
        self._salario = salario

    @property
    def nome(self):
        """declaracao do nome"""
        return self._nome

    @property
    def salario(self):
        """declaracao do salario"""
        return self._salario

    def idade(self):
        """declaracao idade"""
        data_quebrada = self._data_nascimento.split('/')
        ano_nascimento = data_quebrada[-1]
        ano_atual = date.today().year
        return ano_atual - int(ano_nascimento)

    def sobrenome(self):
        """separa o nome por espaco"""
        nome_sperado = self._nome.strip()
        nome_quebrado = nome_sperado.split(' ')
        # ultimo item da lista
        return nome_quebrado[-1]

    def _eh_socio(self):
        """verifica se eh socio"""
        sobrenomes = ['Silva', 'Yakult', 'Silveira', 'Barbosa']
        return ( self._salario >= 1000) and (self.sobrenome() in sobrenomes)

    def decrescimo_salario(self):
        """decrescimo salario"""
        if self._eh_socio():
            decrescimo = self._salario * 0.1
            self._salario = self._salario - decrescimo

    def calcular_bonus(self):
        """declaracao bonus"""
        valor = self._salario * 0.1
        if valor > 1000:
            raise ValueError('O bonus somente aplicado em salarios maior que 1.000')
        return valor

    def __str__(self):
        return f'Funcionario({self._nome}, {self._data_nascimento}, {self._salario})'
