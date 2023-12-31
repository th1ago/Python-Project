"""Criando validador de CPF"""
from validate_docbr import CPF, CNPJ

class Documento:
    """criando class documento"""
    @staticmethod
    def criar_documento(documento):
        """e"""
        doc_str = str(documento)
        if len(doc_str) == 11:
            return DocCpf(doc_str)
        elif len(doc_str) == 14:
            return DocCnpj(doc_str)
        else:
            raise ValueError("Quantidade digitos incorretos")

class DocCpf:
    """verificando o cpf"""
    def __init__(self, documento):
        if self.valida(documento):
            self.cpf = documento
        else:
            raise ValueError("CPF invlaido")

    def __str__(self):
        return self.format()

    def valida(self, documento):
        """validando o cpf"""
        validador = CPF()
        return validador.validate(documento)

    def format(self):
        """formatando o cpf"""
        mascara = CPF()
        return mascara.mask(self.cpf)

class DocCnpj:
    """verificando o cnpj"""
    def __init__(self, documento):
        if self.valida(documento):
            self.cnpj = documento
        else:
            raise ValueError("CPF invlaido")

    def __str__(self):
        return self.format()

    def valida(self, documento):
        """validando o cnpj"""
        validador = CNPJ()
        return validador.validate(documento)

    def format(self):
        """formatando o cnpj"""
        mascara = CNPJ()
        return mascara.mask(self.cnpj)
