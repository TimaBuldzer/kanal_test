import datetime
import os.path
from decimal import Decimal
from typing import List, Any

from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from pydantic import BaseModel

from apps.tsb_rf.parser import TsbRfParser
from conf.settings.google_api_conf import SCOPES, RANGE_NAME, SPREADSHEET_ID


class OrderData(BaseModel):
    external_id: int
    price_usd: Decimal
    price_rub: Decimal
    delivery_dt: datetime.date


class SpreadSheetParser:

    def get_orders_data(self) -> List[OrderData]:
        spreadsheet = self.__request_spreadsheet()
        orders_data = self.__parse_spreadsheet(spreadsheet)
        return orders_data

    @staticmethod
    def __parse_spreadsheet(spreadsheet_value: List[Any]) -> List[OrderData]:
        currency = TsbRfParser().get_usd_currency()
        orders_data: List[OrderData] = list()
        for row in spreadsheet_value:
            try:
                orders_data.append(OrderData(
                    external_id=row[1],
                    price_usd=Decimal(row[2]),
                    price_rub=Decimal(row[2]) * currency.value,
                    delivery_dt=datetime.datetime.strptime(row[3], '%d.%m.%Y').date()
                ))
            except IndexError:
                continue
        return orders_data

    @staticmethod
    def __request_spreadsheet() -> List[OrderData]:
        if os.path.exists('token.json'):
            creds = Credentials.from_authorized_user_file('token.json', SCOPES)
        else:
            raise Exception('You need to authorize first')

        try:
            service = build('sheets', 'v4', credentials=creds)

            # Call the Sheets API
            sheet = service.spreadsheets()
            result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range=RANGE_NAME).execute()
            values = result.get('values', [])

            if not values:
                print('No data found.')
                return []
            return values
        except HttpError as err:
            raise Exception(err)
