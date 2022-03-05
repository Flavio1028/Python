from cpfCnpj import Documento
from TelefonesBr import TelefonesBr
from DatasBr import DatasBr
from acesso_cep import BuscaEndereco

# 15316264754
cpf = 15316264754
objeto_cpf = Documento.cria_documento(cpf)

print(objeto_cpf)

cnpj = 61149239000112
objeto_cnpj = Documento.cria_documento(cnpj)

print(objeto_cnpj)

telefone = "551156481234"

telefone_objeto = TelefonesBr(telefone)
print(telefone_objeto)

cadastro = DatasBr()
cadastro.format_data()
print(cadastro.tempo_cadastro())

cep = "75712450"
objeto_cep = BuscaEndereco(cep)
print(objeto_cep.acessa_via_cep())

