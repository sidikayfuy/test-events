# Тестовое задание "События"

# Запуск:
Создаем виртуальное окружение
```
python -m venv venv
```
Активируем виртуальное окружение
```
"source venv/bin/activate" Linux или ". .\venv\Scripts\activate" для Windows
```
Устанавливаем зависимости
```
pip install -r requirements.txt
```
Далее создаем файл .env и создаем в нем переменные:
```
SECRET_KEY=любой секретный ключ
DB_HOST=хост БД
DB_NAME=имя БД
DB_PORT=порт БД
DB_USER=пользователь БД
DB_PASSWORD=пароль пользователя БД
```
Запускаем проект
```
python manage.py runserver
```

# API
Для регистрации выполнить POST запрос на /api/registration/, передав в теле username, first_name, last_name, password, birthdate (в формате "YYYY-MM-DD")

Авторизация реализована по JWT токену, чтобы его получить необходимо сделать POST запрос на /api/auth/token/, в теле передать username и password.

Использовать токен как заголовок Authorization приписав вначале "Bearer " (Пример "Bearer ashdj21kej1heaskj...")

Для создания события выполнить POST запрос на /api/events/ в теле передавать title, text и date

Для получения списка событий выполнить GET запрос на /api/events/

Для удаления своего события выполнить DELETE запрос на /api/events/ID_СОБЫТИЯ/ написав вместо ID_СОБЫТИЯ, ID события для удаления

Для участия в событии выполнить GET запрос на /api/events/ID_СОБЫТИЯ/join/ написав вместо ID_СОБЫТИЯ, ID события в котором необходимо участвовать

Для отмены участия в событии выполнить GET запрос на /api/events/ID_СОБЫТИЯ/disjoin/ написав вместо ID_СОБЫТИЯ, ID события в котором необходимо отменить участие

