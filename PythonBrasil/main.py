"""testando"""
from cpf_cnpj import Documento

exemplo_cpf = "12815517086"
exemplo_cnpj = "35379838000112"

documento = Documento.criar_documento(exemplo_cnpj)
print(documento)
