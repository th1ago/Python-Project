"""testando"""
# from cpf_cnpj import Documento
# exemplo_cpf = "12815517086"
# exemplo_cnpj = "35379838000112"
# documento = Documento.criar_documento(exemplo_cnpj)
# print(documento)

# from TelefoneBr import TelefoneBr
# telefone = "213326481234"
# telefone_objeto = TelefoneBr(telefone)
# print(telefone_objeto)

# from datas import datas
# cadastro = datas()
# print(cadastro.tempo_cadastro())

from cep import busca_cep

cep = "01001000"
obj_cep = busca_cep(cep)

bairro, cidade, uf = obj_cep.acessa_cep()

print(bairro, cidade, uf)
