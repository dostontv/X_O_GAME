import os

from dotenv import load_dotenv

load_dotenv('.env')


class BotConfig:
    TOKEN = os.getenv('TOKEN')
    WEB_SERVER_HOST = os.getenv('WEB_SERVER_HOST')
    WEB_SERVER_PORT = int(os.getenv('WEB_SERVER_PORT'))
    WEBHOOK_PATH = os.getenv('WEBHOOK_PATH')
    WEBHOOK_SECRET = os.getenv('WEBHOOK_SECRET')
    BASE_WEBHOOK_URL = os.getenv('BASE_WEBHOOK_URL')

    CHANNEL_ID = os.getenv('CHANNEL_ID')
