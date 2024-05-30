# Проект "Журнал оценок"

Проект для управления оценками учеников с использованием FastAPI.

## Запуск проекта

1. Установите зависимости:

    ```bash
    pip install -r requirements.txt
    ```

2. Создайте файл `.env` и добавьте в него следующие переменные окружения:

    ```plaintext
    DATABASE_URL=postgresql://user:password@localhost:5432/gradebook
    ```

3. Запустите приложение:

    ```bash
    python main.py
    ```

После этого приложение будет доступно по адресу `http://localhost:8000`.

## Документация API

Документация API доступна по адресу `http://localhost:8000/docs`.

## Тестирование API

Вы можете использовать инструменты для тестирования API, такие как [Postman](https://www.postman.com/) или `curl`, чтобы отправлять запросы к вашему API. Например:

```bash
curl -X GET "http://localhost:8000/students/1" -H "accept: application/json"
