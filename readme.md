# py-ci-cd
![example workflow](https://github.com/koshi8bit/py-ci-cd/actions/workflows/deploy.yml/badge.svg)

Настройка CI CD для проекта на питоне в github

Пуш в мастер запрещен. В мастер можно фигачить только через *pull request*. Настройка этой опции
[тут](https://github.com/koshi8bit/py-ci-cd/settings/branches)

При пулл реквесте в *master* происходит прогон пайплайна, описанного [тут](.github/workflows/python-app.yml).
В него входит
- Инициализация нужной версии python
- Установка всех зависимостей из requirements.txt
- Проверка синтаксиса кода по PEP8 при помощи flake8
- Запуск тестов
- Если текущая ветка - мастер и все шаги выше пройдены, тогда:
  - Запаковка кода в докер контейнер
  - Пуш в dockerhub

## Источники
- [Actions](https://youtu.be/WTofttoD2xg?t=82)
- [Docker + Actions](https://youtu.be/09lZdSpeHAk?t=80)
- [Actions на русском](https://youtu.be/hevU4NdIsoU)
- [Gitlab docker](https://youtu.be/RV0845KmsNI)

