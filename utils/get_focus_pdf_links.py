from datetime import datetime, timedelta
import requests

class GetFocusPdfLinks:
    def get_data(self) -> list:
        url = 'https://www.bcb.gov.br/api/servico/sitebcb/focus/ultimas?quantidade=1000&filtro='
        response = requests.get(url)
        data = response.json()
        data = data['conteudo']
        data = list(map(lambda x: {'releaseDate': self.__next_monday_date(x['DataReferencia']), 'url': f"https://www.bcb.gov.br{x['Url']}"}, data))
        return data
    
    def __next_monday_date(self, date_str):
        date = datetime.strptime(date_str[:10], '%Y-%m-%d')
        days_ahead = 0 - date.weekday() + 7
        next_monday = date + timedelta(days=days_ahead)
        return next_monday.strftime('%Y-%m-%d')
