from cpfCnpj import Documento
from TelefonesBr import TelefonesBr

# 15316264754
cpf = 15316264754
objeto_cpf = Documento.cria_documento(cpf)

print(objeto_cpf)

cnpj = 61149239000112
objeto_cnpj = Documento.cria_documento(cnpj)

print(objeto_cnpj)

telefone = "11956481234"

telefone_objeto = TelefonesBr(telefone)
print(telefone_objeto)