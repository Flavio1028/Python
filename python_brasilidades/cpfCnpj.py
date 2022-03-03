from validate_docbr import CNPJ
from validate_docbr import CPF

class Documento:

    @staticmethod
    def cria_documento(documento):
        documento = str(documento)
        if len(documento) == 11:
            return DocCpf(documento)
        elif len(documento) == 14:
            return DocCnpj(documento)
        else:
            raise ValueError("Quantidade de dígitos esta incorreta!!")

class DocCpf:
    def __init__(self, documento):
        if self.valida(documento):
            self.cpf = documento
        else:
            raise ValueError("CPF inválido!")

    def valida(self, documento):
        return CPF().validate(documento)

    def format(self):
        return CPF().mask(self.cpf)

    def __str__(self):
        return self.format()

class DocCnpj:
    def __init__(self, documento):
        if self.valida(documento):
            self.cnpj = documento
        else:
            raise ValueError("CNPJ inválido!")

    def valida(self, documento):
        return CNPJ().validate(documento)

    def format(self):
        return CNPJ().mask(self.cnpj)

    def __str__(self):
        return self.format()


