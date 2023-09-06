"""Criando validador de CPF"""
from validate_docbr import CPF, CNPJ

class Documento:
    """e"""
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
    """e"""
    def __init__(self, documento):
        if self.valida(documento):
            self.cpf = documento
        else:
            raise ValueError("CPF invlaido")

    def __str__(self):
        return self.format()

    def valida(self, documento):
        """e"""
        validador = CPF()
        return validador.validate(documento)

    def format(self):
        """e"""
        mascara = CPF()
        return mascara.mask(self.cpf)

class DocCnpj:
    """e"""
    def __init__(self, documento):
        if self.valida(documento):
            self.cnpj = documento
        else:
            raise ValueError("CPF invlaido")

    def __str__(self):
        return self.format()

    def valida(self, documento):
        """e"""
        validador = CNPJ()
        return validador.validate(documento)

    def format(self):
        """e"""
        mascara = CNPJ()
        return mascara.mask(self.cnpj)
