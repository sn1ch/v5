import gspread
from google.oauth2.service_account import Credentials


MSG_INFO = 'Перед вами актуальный ассортимент крафтового пива в нашем баре. Выбирайте любимые позиции и на этапе' \
           ' заказа (кнопка «сделать заказ») пишите нам название и количество, и мы подготовим ваш заказ к указанному' \
           ' времени.'


def take_bakunin_beers(gs_json, url):
    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']
    credentials = Credentials.from_service_account_file(gs_json, scopes=scope)
    gc = gspread.authorize(credentials)
    sh = gc.open_by_url(url)
    worksheet = sh.get_worksheet(0)
    all_beers = worksheet.get_all_values()
    actual_beers = []
    for beer in all_beers:
        if beer[0] == 'TRUE':
            actual_beers.append(beer[1:])
    return actual_beers


def take_import_beers(gs_json, url):
    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']
    credentials = Credentials.from_service_account_file(gs_json, scopes=scope)
    gc = gspread.authorize(credentials)
    sh = gc.open_by_url(url)
    worksheet = sh.get_worksheet(1)
    all_beers = worksheet.get_all_values()
    return all_beers[1:]


def take_russian_beers(gs_json, url):
    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']
    credentials = Credentials.from_service_account_file(gs_json, scopes=scope)
    gc = gspread.authorize(credentials)
    sh = gc.open_by_url(url)
    worksheet = sh.get_worksheet(2)
    all_beers = worksheet.get_all_values()
    return all_beers[1:]
