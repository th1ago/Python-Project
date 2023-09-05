"""testando"""
from cpf_cnpj import CpfCnpj

exemplo_cpf = "12815517086"
exemplo_cnpj = "35379838000112"

documento = CpfCnpj(exemplo_cpf, 'cpf')
print(documento)
