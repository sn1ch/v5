import os
from dotenv import load_dotenv
load_dotenv()

TOKEN = os.getenv('TOKEN')
GS_JSON = os.getenv('GS_JSON')

URL_BAKUNIN = os.getenv('URL_BAKUNIN')
URL_KIOSK = os.getenv('URL_KIOSK')
URL_STEREO = os.getenv('URL_STEREO')
URL_ROKETS = os.getenv('URL_ROKETS')

ORDER_CHAT_BAKUNIN = os.getenv('ORDER_CHAT_BAKUNIN')
ORDER_CHAT_STEREO = os.getenv('ORDER_CHAT_STEREO')
ORDER_CHAT_KIOSK = os.getenv('ORDER_CHAT_KIOSK')
ORDER_CHAT_ROKETS = os.getenv('ORDER_CHAT_ROKETS')
