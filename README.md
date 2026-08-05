# Django Netology HW

Django-проект с REST API, подготовленный для запуска в Docker-контейнере.

---

# Требования

Перед запуском необходимо установить:

- **Python 3.x**
- **Docker Desktop**

---

# Запуск проекта локально

## Установка зависимостей

```bash
pip install -r requirements.txt
```

## Запуск Django-сервера

```bash
python manage.py runserver
```

После запуска приложение доступно:

[http://127.0.0.1:8000](http://127.0.0.1:8000)

---

# Запуск проекта в Docker

## 1. Сборка Docker image

Перейти в корневую папку проекта, где находится файл:

```
Dockerfile
```

Выполнить:

```powershell
docker build -t django-netology:1.0 .
```

После успешной сборки проверить созданный образ:

```powershell
docker images
```

Пример:

```
REPOSITORY          TAG
django-netology     1.0
```

---

# Запуск Docker-контейнера

Запуск Django backend-сервера:

```powershell
docker run -d `
  --name django_api `
  --env-file .env `
  -p 8000:8000 `
  django-netology:1.0
```

## Описание параметров

| Параметр | Назначение |
|---|---|
| `-d` | запуск контейнера в фоновом режиме |
| `--name django_api` | имя контейнера |
| `--env-file .env` | передача переменных окружения |
| `-p 8000:8000` | проброс порта компьютера в контейнер |
| `django-netology:1.0` | имя Docker image |

После запуска приложение доступно:

[http://localhost:8000](http://localhost:8000)

---

# Проверка работы контейнера

## Список запущенных контейнеров

```powershell
docker ps
```

## Список всех контейнеров

```powershell
docker ps -a
```

---

# Работа с логами

## Просмотр логов контейнера

```powershell
docker logs django_api
```

## Просмотр логов в реальном времени

```powershell
docker logs -f django_api
```

---

# Управление контейнером

## Остановка контейнера

```powershell
docker stop django_api
```

---

## Удаление контейнера

Если контейнер остановлен:

```powershell
docker rm django_api
```

Если контейнер запущен:

```powershell
docker rm -f django_api
```

---

# Пересборка проекта после изменений

После изменения кода необходимо пересобрать Docker image.

## 1. Удалить старый контейнер

```powershell
docker rm -f django_api
```

---

## 2. Пересобрать Docker image

```powershell
docker build -t django-netology:1.0 .
```

---

## 3. Запустить новый контейнер

```powershell
docker run -d `
  --name django_api `
  --env-file .env `
  -p 8000:8000 `
  django-netology:1.0
```

---

# Environment variables (.env)

Настройки проекта хранятся в файле:

```
.env
```

Файл `.env` не копируется в Docker image и передается отдельно при запуске контейнера:

```powershell
--env-file .env
```

Используемые переменные:

```env
SECRET_KEY
DEBUG
ALLOWED_HOSTS

DB_ENGINE
DB_NAME
DB_HOST
DB_PORT
DB_USER
DB_PASSWORD
```

---

# Проверка работы API

Через браузер:

[http://localhost:8000](http://localhost:8000)


Через командную строку:

```powershell
curl.exe http://localhost:8000
```

---

# Полезные Docker команды

## Список Docker images

```powershell
docker image ls
```

---

## Удаление Docker image

```powershell
docker rmi django-netology:1.0
```

---

## Информация о контейнере

```powershell
docker inspect django_api
```

---

## Подключение к контейнеру

Открыть shell внутри контейнера:

```powershell
docker exec -it django_api bash
```

---

## Просмотр файлов внутри контейнера

```bash
ls -la /app
```

---

# Текущая архитектура запуска

```
Windows PC

    |
    |
    |  localhost:8000
    |
    v

Docker Container

    |
    |
    |  Django runserver
    |
    v

/app/manage.py
```

---

# Следующий этап развития проекта

Планируемые улучшения:

- подключение `db.sqlite3` через Docker volume;
- переход на PostgreSQL;
- добавление `docker-compose`;
- запуск через Gunicorn;
- добавление Nginx как reverse proxy.