import requests

from conf.settings.telegram_conf import BOT_TOKEN


class TelegramBot:
    def send_message(self, chat_id: int, text: str) -> None:
        url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={text}'
        requests.post(url)
