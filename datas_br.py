import datetime
from datetime import datetime, timedelta

class DatasBr:
    def __init__(self):
        self._momento_cadastro = datetime.today()

    def mes_cadastro(self):
        meses_do_ano = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
        mes_cadastro = self._momento_cadastro.month
        return meses_do_ano[mes_cadastro - 1]

    def dia_semana(self):
        dia_semana_ano = ["segunda", "terça", "quarta", "quinta", "sexta", "sabado", "domingo"]
        return dia_semana_ano[self._momento_cadastro.weekday() - 1]

    def format_data(self):
        self._momento_cadastro.strftime("%d/%m/%Y %H:%M")

    def __str__(self):
        return self.format_data()

    def tempo_cadastro(self):
        return (datetime.today() + timedelta(days = 30))- self._momento_cadastro