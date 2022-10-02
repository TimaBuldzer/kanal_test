import os

SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

# The ID and range of a sample spreadsheet.
SPREADSHEET_ID = os.environ.get('SPREADSHEET_ID', '1tuqwgTcfv5iTY9jPi57y4HEOgEKZRVcfJPz3bFg0u44')
RANGE_NAME = 'Sheet!A2:D'
