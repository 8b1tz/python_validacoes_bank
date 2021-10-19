import requests


class AcessoApiCep:

    def __init__(self, cep):
        cep = str(cep)
        if self.cep_eh_valido(cep):
            self.__cep = cep
        else:
            raise ValueError("CEP inválido")

    def __str__(self):
        return self.format_cep()

    def cep_eh_valido(self, cep):
        return True if len(cep) == 8 else False

    def format_cep(self):
        return f"{self.__cep[:4]}-{self.__cep[5:]}"

    def acessa_via_cep(self):
        url = f"https://viacept.com.br/ws/{self.format_cep()}/json/"
        r = requests.get(url)
        dados = r.json()
        return (
            dados["bairro"],
            dados["localidade"],
            dados["uf"]
        )