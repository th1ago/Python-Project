"""Criando validador de CPF"""

class Cpf:
    """criando o inicializador"""
    def __init__(self, documento):
        self.documento = str(documento)
        if self.cpf_eh_valido(documento):
            self.cpf = documento
        else:
            raise ValueError("CPF inválido!")

    def __str__(self):
        return self.format_cpf()

    def cpf_eh_valido(self, documento):
        """validando o cpf"""
        if len(documento) == 11:
            return True
        else:
            return False

    def format_cpf(self):
        """formatando o cpf"""
        fatia_um = self.cpf[:3]
        fatia_dois = self.cpf[3:6]
        fatia_tres = self.cpf[6:9]
        fatia_quatro = self.cpf[9:]

        return f" {fatia_um}-{fatia_dois}-{fatia_tres}-{fatia_quatro}"
