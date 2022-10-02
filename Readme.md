### Тестовое задание для КаналСервис

Все токены и ключи для доступа к API являются тестовыми и не несут в себе никакой ценности).

## Задание

https://unwinddigital.notion.site/unwinddigital/Python-1fdcee22ef5345cf82b058c333818c08

## Для запуска

1. Необходимо установить зависимости из файла requirements.txt
2. Авторизоваться в Google API с помощью следующей команды(запускать в любом линуксовом терминале):
```bash
./authorize.sh
```
4. Стартануть бота @some_some_test_bot в Telegram
5. Запустить проект с помощью команды:
```bash
docker-compose up
```
4. Подключиться к контейнеру приложения с помощью
```bash
docker exec -it kanal_test_web_1 bash
```
5. Создать пользователя с помощью
```bash
python manage.py createsuperuser
```

7. Приложение будет доступно по адресу http://localhost:8000