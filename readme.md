# py-ci-cd
![example workflow](https://github.com/koshi8bit/py-ci-cd/actions/workflows/python-app.yml/badge.svg)

Настройка CI CD для проекта на питоне

Пуш в мастер запрещен. В мастер можно фигачить только через *pull request*. Настройка этой опции
[тут](https://github.com/koshi8bit/py-ci-cd/settings/branches)

При пулл реквесте в *master* происходит прогон пайплайна, описанного [тут](.github/workflows/python-app.yml).
В него входит
- Инициализация нужной версии python
- Установка всех зависимостей из requirements.txt
- Проверка синтаксиса кода по PEP8 при помощи flake8
- Запуск тестов
- Запаковка кода в докер контейнер
- Пуш в dockerhub



