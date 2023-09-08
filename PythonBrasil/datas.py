"""validando datas"""
from datetime import datetime, timedelta

class datas:
    """Iniciando a classe data"""
    def __init__(self) -> None:
        self.momento_cadastro = datetime.today()

    def __str__(self):
        """retorno da data"""
        return self.format_data()

    def mes_cadastro(self):
        """lista do meses"""
        meses_do_ano = [
            "janeiro", "fevereiro", "marco",
            "abril", "maio", "junho", "julho",
            "agosto", "setembro", "outubro",
            "novembro", "dezembro"
        ]
        mes_corrente = self.momento_cadastro.month -1
        return meses_do_ano[mes_corrente]

    def dia_semana(self):
        """lista dos dias da semana"""
        dia_semana_lista = [
            "segunda", "terca", "quarta",
            "quinta", "sexta", "sabado",
            "domingo"
        ]
        dia_semana = self.momento_cadastro.weekday()
        return dia_semana_lista[dia_semana]

    def format_data(self):
        """formatando padra br"""
        # dias do mes
        # meses em formato numerio
        # Ano em formato de 4 digitos
        # Hora em formato decimal
        # Minutos em formato decimal
        data_formatada = self.momento_cadastro.strftime("%d/%m/%Y %H:%M")
        return data_formatada

    def tempo_cadastro(self):
        """realiza a subtracao"""
        tempo_cadastro = (datetime.today() + timedelta(days=30)) - self.momento_cadastro
        return tempo_cadastro