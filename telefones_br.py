import re
class TelefonesBr:
    def __init__(self, telefone):
        if self.valida_telefone(telefone):
            self.__numero = telefone
        else:
            raise ValueError("Número incorreto!")

    def valida_telefone(self, telefone):
        padrao = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
        resposta = re.findall(padrao, telefone)
        if resposta:
            return True
        return False

    def format_numero(self, numero):
        padrao = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
        resposta = re.search(padrao, numero)
        return f"+{resposta.group(1)} ({resposta.group(2)}) {resposta.group(3)}-{resposta.group(4)}"

    def __str__(self):
        return self.format_numero(self.__numero)