# py-ci-cd
[![Tests and deploy](https://github.com/koshi8bit/py-ci-cd/actions/workflows/deploy.yml/badge.svg)](https://github.com/koshi8bit/py-ci-cd/actions/workflows/deploy.yml)

Настройка CI CD для проекта на python в github

Пуш в мастер запрещен. В мастер можно фигачить только через *pull request*. Настройка этой опции
[тут](https://github.com/koshi8bit/py-ci-cd/settings/branches)

Перед pull реквестом в *master* происходит прогон пайплайна, описанного [тут](.github/workflows/deploy.yml).
В него входит:
- Инициализация нужной версии python
- Установка всех зависимостей из requirements.txt
- Проверка синтаксиса кода по PEP8 при помощи flake8
- Запуск [юнит тестов](tests/test_app.py)
 
Перед пушем в мастер происходит все, что описано выше, но добавляется процесс деплоя на хостинг:
- Запаковка кода в docker контейнер.
- Пуш в dockerhub. При этом образ имеет вид `username/container_name-branch_name:commit_hash`. 
  Такой подход позволит легко вернуться в рабочую версию в случае горения жёп.
- Создание контейнера в виде файла и сжатие его перед отправкой на хостинг (устарело, загрузка в dockerhub лучше, т.к.
  тогда заливается только diff. Но если интересно - можно посмотреть шаги в файле _.github\workflows\deploy.yml.7z_ на этапе _Create locally_).
- Отправка архива контейнера на хостинг через csp (устарело, см выше).
- Подготовка приватного SSH ключа для хостинга из "секретов" гитхаба.
- В этом пайпе представлены примеры удалённого запуска кода на хостинге и пример передачи файла
- Запуск docker контейнера на хостинге при помощи `docker-compose` через SSH. Рабочий развернутый проект [на хостинге amazon](http://ec2-18-220-152-128.us-east-2.compute.amazonaws.com:5000/api/v2/foo). Исходный код [тут](src/main.py) **В МОЕМ ПРИМЕРЕ ОТКЛЮЧЁН HTTPS!** 
- PROFIT!!

Проект и документацию сделал **Лёха К** aka **koshi8bit** 

## Branch protection rule
Branch protection rule для веток ниже будет таким: `[dps][ert][voa]*`:
- dev
- prod
- stage

Абсолютно отвратительный паттерн, который берет 3 раза по каждой букве каждой ветки. Паттерн передается в _fnmatch_, 
который не умеет в _или_. По сути - урезанная регулярка.

## Источники
- [Actions](https://youtu.be/WTofttoD2xg?t=82)
- [Docker + Actions](https://youtu.be/09lZdSpeHAk?t=80)
- [Actions на русском](https://youtu.be/hevU4NdIsoU)
- [Gitlab docker](https://youtu.be/RV0845KmsNI)
- [Моя таблица с командами для Docker](https://docs.google.com/spreadsheets/d/1XWuif-QDWUb66IGFz_dPtnHq3K8sGVm4_GctkrrSni4/edit#gid=882078486)