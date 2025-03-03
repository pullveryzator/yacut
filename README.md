# YaCut

YaCut — это сервис укорачивания ссылок, который позволяет пользователям ассоциировать длинные URL с короткими. Пользователи могут предоставить собственный вариант короткой ссылки или позволить сервису сгенерировать ее автоматически.

## Ключевые возможности

- Генерация коротких ссылок и их связь с исходными длинными ссылками.
- Переадресация на исходный адрес при обращении к коротким ссылкам.
- Пользовательский интерфейс с простой формой для создания коротких ссылок.

## Пользовательский интерфейс

Сервис представляет собой одну страницу с формой, состоящей из двух полей:

- **Длинная исходная ссылка** (обязательное поле).
- **Пользовательская короткая ссылка** (необязательное поле, не более 16 символов).

Если пользователь не укажет собственный вариант короткой ссылки, сервис автоматически сгенерирует ее. Формат для авто-сгенерированной ссылки — шесть случайных символов, которые могут включать:

- Большие латинские буквы (A-Z)
- Маленькие латинские буквы (a-z)
- Цифры (0-9)

Автоматически сгенерированная короткая ссылка добавляется в базу данных только, если в ней еще нет такого же идентификатора. В противном случае генерируется новый идентификатор.

## API

Сервис предоставляет два эндпоинта:

1. **POST /api/id/** - создание новой короткой ссылки.
   - Запрос должен содержать длинную исходную ссылку и необязательную короткую ссылку.

2. **GET /api/id/<short_id>/** - получение оригинальной ссылки по указанному короткому идентификатору.

## Установка

Для запуска проекта необходимо:

1. Клонировать репозиторий:
   
bash
git clone git@github.com:pullveryzator/yacut.git
cd Yacut


2. Установить необходимые зависимости:
   
bash
pip install -r requirements.txt


3. Запустить сервис:
   
bash
flask run


## Использование

При открытии сервиса в браузере пользователь увидит форму для введения длинной ссылки и не обязательного поля для короткой ссылки. После ввода данных и отправки формы, пользователю на странице будет предоставлена короткая ссылка, при нажатии на которую он будет перенаправлен на оригинальный адрес.
