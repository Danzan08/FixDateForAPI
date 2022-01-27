import re
import requests

# Адрес и порт API ЕЦП
ipECP = '91.107.66.210' #ip адрес ЕЦП
portECP = '8087' #порт

# Данные региона
username = 'username' #Логин от API ЕЦП
password = 'password' #Пароль от API ЕЦП
kladr = 'your kladr region' #0800000000000 Кладр Калмыкии

# Настройка прокси
proxySettings = {
    "http": "http://192.168.0.100:3128",
}

# Генерируем URL
url = 'http://' + ipECP + ':' + portECP + '/app/api/export/GetRequestsClientJobless?regionCode=' + kladr

# Генерируем токен для авторизации (base64login)
session = requests.Session()
session.auth = (username, password)

# Отправляем get запрос, проверяем есть ли настройки прокси
if proxySettings:
    response = session.get(url, proxies=proxySettings)
else:
    response = session.get(url)

if (response.status_code == 200):
    # Сохраняем оригинал
    originalResponseFile = open('GetRequestsClientJobless(original).xml', 'w')
    originalResponseFile.write(response.text)
    originalResponseFile.close()

    # Регулярка для поиска timestamp вместо date
    regex = re.compile('(<benefitPaymentStartDate>|<cvDateFrom>)(\d{4}-\d{2}-\d{2}\w\\d{2}:\\d{2}:\\d{2}\w)', re.S)

    # Проверяем benefitPaymentStartDate и cvDateFrom, если есть совпадения вырезаем 10 символов с конца (время T00:00:00Z)
    responseModified = regex.sub(lambda m: m.group()[:-10], response.text)

    # Сохраняем файл изменений
    modifiedResponseFile = open('GetRequestsClientJobless(modified).xml', 'w')
    modifiedResponseFile.write(responseModified)
    modifiedResponseFile.close()
    print('Success.')
else:
    print('Нет соединения с api, статус ошибки: ' + response.status_code)
