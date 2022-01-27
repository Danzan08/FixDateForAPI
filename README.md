# Фикс даты в запросах api c портала ЕЦП

## Для выгрузки запросов, необходимо:

- Для запуска скрипта, необходимо установить python3 (https://www.python.org/downloads/)
- Введите свои данные в файле скрипта (поля username, password и kladr) для загрузки get-запросов
- С помощью командной строки запустить данный скрипт (пример ./python3 main.py)
- В папке рядом со скриптом должны появиться два файла GetRequestsClientJobless(original).xml и GetRequestsClientJobless(modified).xml
- Для проверки работоспособности можете сверить два файла плагином Compare в Notepad++ (https://techblog.sdstudio.top/kak-sravnit-dva-tekstovyh-fajla-s-pomoshhju-notepad/)

### Исходный код скрипта открыт, Вы можете убедиться в его безопасности, открыв его в блокноте или на странице github. 
### Прошу обратить внимание, что при загрузке в Катарсис необходимо полностью убедиться что файл валиден (Метод Compare в Notepad++, который я описал выше)
