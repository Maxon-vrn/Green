Описание работы,структуры и развертывания этого приложения.


uvicorn main:app --reload  - старт локального сервера

Интерактивная документация API будет автоматически обновляться, включая новое тело: http://127.0.0.1:8000/docs.
Альтернативная документация также будет отражать новый параметр и тело запроса: http://127.0.0.1:8000/redoc.

Команды для работы с сервисом:
alembic init migrations - создается каталог migrations и файл alembic.ini
alembic revision --autogenerate -m "Database creation" - создаем версию миграции
alembic upgrade 4bdcd9a9f593 - проводим миграцию и указываем номер ривизии из каталога migration/version/'file'
    - (ищем строку с номером ревизии: revision: str = '4bdcd9a9f593')
alembic upgrade head - апгрейд до последней ревизии




SQL command and text:
- insert into role values (1,'user',null),(2,'worker',null),(3,'admin',null);(4,'foreman',null)
- select * from role;




Структура каталогов:
- cred - креды для доступа 
- db - даза данных
- src -
- template - шаблоны статичных файлов
    -css
    -html
    -js
- images - изображения
- tests - все модульные тесты и другое

- main - файл логики обработки страниц
- requirements - файл зависимостей библиотек для запуска и разворачивания скрипта

- task - файл постановки задач на день и\или неделю