from validate_docbr import CPF, CNPJ


class Documento:

    @staticmethod
    def cria_documento(documento):
        if len(documento) == 11:
            return DocCpf(documento)
        elif len(documento) == 14:
            return DocCnpj(documento)
        else:
            raise ValueError("QUANTIDADE DE DIGITOS INVÁLIDOS")


class DocCpf():

    def __init__(self, documento):
        if self.valida(documento):
            self._cpf = documento
        else:
            raise ValueError("CPF INVÁLIDO")

    def valida(self, documento):
        return CPF().validate(documento)

    def format(self):
        return CPF().mask(self._cpf)

    def __str__(self):
        return self.format()


class DocCnpj:
    def __init__(self, documento):
        if self.valida(documento):
            self._cnpj = documento
        else:
            raise ValueError("CNPJ inválido")

    def valida(self, documento):
        return CNPJ().validate(documento)

    def format(self):
        return CNPJ().mask(self._cnpj)

    def __str__(self):
        return self.format()
