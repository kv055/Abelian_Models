import PriceData.find_parent
from Database_SQL.aws_sql_connect import SQL_Server


class Querry_Assets_OHLC_from_DB:
    def __init__(self) -> None:
        self.db_name = 'DummyData'
        self.db_connection = SQL_Server(self.db_name)

    def return_historical_average_from_db(self,asset_dict):
        ticker = asset_dict['ticker']
        data_provider = asset_dict['data_provider']
        query = f"""
            SELECT 
                UNIX_TIMESTAMP(Date) AS Timestamp, close 
            FROM {self.db_name}.OHLC
            WHERE data_provider = '{data_provider}' and ticker = '{ticker}'
        """
        self.db_connection.cursor.execute(query)
        table = self.db_connection.cursor.fetchall()
        return table

    def return_historical_ohlc_from_db(self, asset_dict):
        ticker = asset_dict['ticker']
        data_provider = asset_dict['data_provider']
        query = f"""
            SELECT 
                UNIX_TIMESTAMP(Date) AS Timestamp,Open,High,Low,Close 
            FROM {self.db_name}.OHLC
            WHERE data_provider = '{data_provider}' and ticker = '{ticker}'
        """
        self.db_connection.cursor.execute(query)
        table = self.db_connection.cursor.fetchall()
        return table
    