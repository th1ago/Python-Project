"""validando telefoens brasil"""
import re

class TelefoneBr:
    """verifica telefone"""
    def __init__(self, telefone):
        if self.valida_telefone(telefone):
            self.numero = telefone
        else:
            raise ValueError("Numero incorreto")

    def __str__(self):
        """representacao string da classe """
        return self.format_numero()

    def valida_telefone(self, telefone):
        """valida telefone"""
        padrao = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
        resposta = re.findall(padrao, telefone)
        if resposta:
            return True
        else:
            return False

    def format_numero(self):
        """retornar o numero formatado"""
        padrao = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
        resposta = re.search(padrao, self.numero)
        return f"+{resposta.group(1)}({resposta.group(2)}){resposta.group(3)}-{resposta.group(4)}"
