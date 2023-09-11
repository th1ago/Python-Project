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

    def calcular_bonus(self):
        """declaracao bonus"""
        valor = self._salario * 0.1
        if valor > 1000:
            valor = 0
        return valor

    def __str__(self):
        return f'Funcionario({self._nome}, {self._data_nascimento}, {self._salario})'
