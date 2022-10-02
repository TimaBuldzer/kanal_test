from decimal import Decimal
from typing import List

import requests

import xmltodict
from pydantic import BaseModel, Field


class Currency(BaseModel):
    id: str = Field(alias='@ID')
    nominal: int = Field(alias='Nominal')
    value: Decimal = Field(alias='Value')


class TsbRfParser:

    def get_usd_currency(self) -> Currency:
        currencies = self.__request_currency_quotes()
        usd = list(filter(lambda x: x.id == 'R01235', currencies))[0]
        return usd

    def __request_currency_quotes(self) -> List[Currency]:
        url = 'https://www.cbr.ru/scripts/XML_daily.asp'
        response = requests.get(url)
        return self.__parse_currency_quotes(response.content)

    @staticmethod
    def __parse_currency_quotes(data: bytes) -> List[Currency]:
        dict_data = xmltodict.parse(data)
        parsed_data = list()
        for currency in dict_data['ValCurs']['Valute']:
            value = currency.pop('Value')
            currency = Currency(Value=Decimal(value.replace(',', '.')), **currency)
            parsed_data.append(currency)
        return parsed_data
