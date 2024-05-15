import yfinance as yf
from datetime import datetime, timedelta

class StockDirection:
    def set_symbol(self, symbol) -> None:
        self.__symbol = symbol

    def set_start_date(self, startDate) -> None:
        self.__startDate = startDate

    def set_end_date(self, endDate) -> None:
        self.__endDate = endDate

    def set_interval(self, interval) -> None:
        self.__interval = interval

    def get_first_candle_direction(self) -> bool:
        data = yf.Ticker(self.__symbol).history(start=self.__startDate, end=self.__get_start_date_plus_one_day(), interval=self.__interval)
        data['upTrend'] = data['Open'] < data ['Close']
        direction = data[['upTrend']].head(1).values[0][0]
        return 1 if direction else -1
    
    def __get_start_date_plus_one_day(self) -> str:
        date_string = self.__startDate
        date = datetime.strptime(date_string, "%Y-%m-%d")
        new_date = date + timedelta(days=1)
        new_date_string = new_date.strftime("%Y-%m-%d")
        return new_date_string
